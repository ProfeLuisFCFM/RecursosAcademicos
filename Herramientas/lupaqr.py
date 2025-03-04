import sys
import cv2
import numpy as np
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import Qt, QTimer
from mss import mss  # Para capturar la pantalla

class QRScanner(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lupa QR")
        self.setGeometry(100, 100, 500, 500)  # Tamaño fijo
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)

        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 400, 300)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_view)
        self.timer.start(100)  # Captura cada 100 ms

        self.sct = mss()

    def update_view(self):
        screenshot = self.sct.grab({"left": self.x(), "top": self.y(), "width": 400, "height": 300})
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

        qimg = QImage(img, img.shape[1], img.shape[0], QImage.Format.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(qimg))

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.scan_qr()

    def scan_qr(self):
        screenshot = self.sct.grab({"left": self.x(), "top": self.y(), "width": 400, "height": 300})
        img = np.array(screenshot)
        gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

        detector = cv2.QRCodeDetector()
        data, _, _ = detector.detectAndDecode(gray)

        if data:
            print(f"QR Detectado: {data}")
        else:
            print("No se detectó QR")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRScanner()
    window.show()
    sys.exit(app.exec())
