import sys
import subprocess
import threading
import time
import os
import base64
import io
from datetime import datetime
import json
import tempfile
import shutil
import py7zr

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar, QPushButton,
    QFileDialog, QMessageBox, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem, QInputDialog
)
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtCore import pyqtSignal, QObject


import fitz  # PyMuPDF
from PIL import Image

class SignalEmitter(QObject):
    done = pyqtSignal()


REQUIRED_PACKAGES = ["PyQt5", "PyMuPDF", "Pillow", "py7zr"]

class InstallerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Preparando entorno...")
        self.setGeometry(100, 100, 400, 100)

        self.layout = QVBoxLayout()

        self.label = QLabel("Verificando e instalando dependencias...")
        self.progress = QProgressBar()
        self.progress.setValue(0)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.progress)
        self.setLayout(self.layout)

        self.show()

        # Signal to communicate with the main thread
        self.signals = SignalEmitter()
        self.signals.done.connect(self.launch_main_app)

        threading.Thread(target=self.install_dependencies).start()


    def install_dependencies(self):
        total = len(REQUIRED_PACKAGES)
        for i, package in enumerate(REQUIRED_PACKAGES):
            if not self.is_installed(package):
                self.label.setText(f"Instalando {package}...")
                self.install_package(package)
            self.progress.setValue(int(((i + 1) / total) * 100))
            time.sleep(0.5)

        self.label.setText("¡Listo! Ejecutando aplicación...")
        time.sleep(1)
        
        # Emitir la señal para lanzar la aplicación principal
        self.signals.done.emit()



    def is_installed(self, package_name):
        try:
            subprocess.check_call([sys.executable, "-c", f"import {package_name}"])
            return True
        except subprocess.CalledProcessError:
            return False

    def install_package(self, package_name):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

    def launch_main_app(self):
        self.close()
        self.main_app = PDFSignerApp()
        self.main_app.show()


class PDFSignerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Firmador PDF Multiformante")
        self.setGeometry(100, 100, 800, 600)

        self.canvas = SignatureCanvas()
        self.setCentralWidget(self.canvas)

        self.toolbar = self.addToolBar("Opciones")
        self.toolbar.addAction("Cargar PDF", self.load_pdf)
        self.toolbar.addAction("Firmar", self.canvas.add_signature)
        self.toolbar.addAction("Guardar Documento Firmado", self.save_signed_doc)

        self.doc = None
        self.current_page = None
        self.pdf_path = None

    def load_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Selecciona un PDF", "", "PDF Files (*.pdf)")
        if file_path:
            self.pdf_path = file_path
            self.doc = fitz.open(file_path)
            self.current_page = 0
            pix = self.doc[self.current_page].get_pixmap()
            img = QImage(pix.samples, pix.width, pix.height, pix.stride, QImage.Format_RGB888)
            self.canvas.set_pdf_image(img)

    def save_signed_doc(self):
        if not self.doc or not self.pdf_path:
            QMessageBox.warning(self, "Advertencia", "Primero carga un PDF.")
            return

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_pdf = os.path.join(temp_dir, "archivo_firmado.pdf")
            temp_json = os.path.join(temp_dir, "archivo_firmado.json")

            for sig in self.canvas.signatures:
                page = self.doc[self.current_page]
                rect = fitz.Rect(sig['posicion']['x'], sig['posicion']['y'],
                                 sig['posicion']['x'] + sig['tamano']['ancho'],
                                 sig['posicion']['y'] + sig['tamano']['alto'])
                image_bytes = base64.b64decode(sig['firma_base64'].split(",")[1])
                img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
                img_path = os.path.join(temp_dir, "temp_signature.png")
                img.save(img_path)
                page.insert_image(rect, filename=img_path)

            self.doc.save(temp_pdf)

            with open(temp_json, "w", encoding="utf-8") as f:
                json.dump({"firmas": self.canvas.signatures}, f, indent=4)

            save_path, _ = QFileDialog.getSaveFileName(self, "Guardar documento firmado", "", "Document Signed (*.dsg)")
            if save_path:
                if not save_path.endswith(".dsg"):
                    save_path += ".dsg"
                with py7zr.SevenZipFile(save_path, 'w') as archive:
                    archive.write(temp_pdf, arcname="documento.pdf")
                    archive.write(temp_json, arcname="firmas.json")

                QMessageBox.information(self, "Éxito", f"Documento firmado guardado como {save_path}")

class SignatureCanvas(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.pdf_item = None
        self.signatures = []

    def set_pdf_image(self, image):
        self.scene.clear()
        self.pdf_item = QGraphicsPixmapItem(QPixmap.fromImage(image))
        self.scene.addItem(self.pdf_item)

    def add_signature(self):
        name, ok = QInputDialog.getText(self, "Firmante", "Nombre del firmante:")
        if not ok or not name:
            return

        sig_img = self.capture_signature()
        if sig_img:
            barray = io.BytesIO()
            sig_img.save(barray, format="PNG")
            base64_img = "data:image/png;base64," + base64.b64encode(barray.getvalue()).decode("utf-8")
            x, y = 100, 100
            self.scene.addPixmap(QPixmap.fromImage(sig_img)).setPos(x, y)

            self.signatures.append({
                "nombre": name,
                "fecha": datetime.now().isoformat(),
                "pagina": 1,
                "posicion": {"x": x, "y": y},
                "tamano": {"ancho": sig_img.width(), "alto": sig_img.height()},
                "firma_base64": base64_img
            })

    def capture_signature(self):
        window = QWidget()
        window.setWindowTitle("Dibuja tu firma")
        layout = QVBoxLayout()
        canvas = SignatureDrawArea()
        btn_ok = QPushButton("Aceptar")
        layout.addWidget(canvas)
        layout.addWidget(btn_ok)
        window.setLayout(layout)

        result = {}

        def accept():
            result['image'] = canvas.get_image()
            window.close()

        btn_ok.clicked.connect(accept)
        window.setGeometry(200, 200, 400, 200)
        window.exec_() if hasattr(window, 'exec_') else window.show()
        app = QApplication.instance()
        while window.isVisible():
            app.processEvents()

        return result.get('image')

class SignatureDrawArea(QWidget):
    def __init__(self):
        super().__init__()
        self.image = QImage(400, 150, QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.last_point = QPoint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.drawing:
            painter = QPainter(self.image)
            pen = QPen(Qt.black, 2, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def get_image(self):
        return self.image

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstallerWindow()
    sys.exit(app.exec_())