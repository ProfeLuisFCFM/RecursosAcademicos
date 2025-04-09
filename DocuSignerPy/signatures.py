# signatures.py

import base64
from datetime import datetime
from PIL import Image
import io

class SignatureManager:
    def __init__(self):
        self.signatures = []

    def add_signature(self, name, image: Image.Image, page: int = 1, x: int = 100, y: int = 100):
        barray = io.BytesIO()
        image.save(barray, format="PNG")
        base64_img = "data:image/png;base64," + base64.b64encode(barray.getvalue()).decode("utf-8")

        signature_data = {
            "nombre": name,
            "fecha": datetime.now().isoformat(),
            "pagina": page,
            "posicion": {"x": x, "y": y},
            "tamano": {"ancho": image.width, "alto": image.height},
            "firma_base64": base64_img
        }
        self.signatures.append(signature_data)
        return signature_data

    def export_json(self):
        return {"firmas": self.signatures}

    def clear(self):
        self.signatures = []

    def get_all(self):
        return self.signatures
