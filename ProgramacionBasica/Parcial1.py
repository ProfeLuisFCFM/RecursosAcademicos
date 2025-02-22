import subprocess, sys
from abc import ABC, abstractmethod


def requisitos():
    libraries = [
        'wget',
        'pyqrcode'
    ]
    for lib in libraries:
        try:
            # Intentamos importar la librería
            __import__(lib)
            print(f"{lib} ya está instalada ✅")
        except ImportError:
            # Si no está instalada, la instalamos
            print(f"Instalando {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            print(f"{lib} instalada correctamente ✅")

# Parcial1.py
from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Problema1(ABC):
    """Problema 1: Invertir una cadena."""

    fallo = None  # Indica si la solución es correcta o no

    @abstractmethod
    def invertir_cadena(self, cadena):
        pass

    @staticmethod
    def check():
        """Evalúa la solución definida por el usuario."""
        try:
            # Obtener la función definida por el usuario en el entorno de Colab
            espacio_usuario = get_ipython().user_ns
            if "invertir_cadena" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'invertir_cadena'.")

            funcion_usuario = espacio_usuario["invertir_cadena"]

            # Validar con pruebas
            assert funcion_usuario("hola") == "aloh"
            assert funcion_usuario("Python") == "nohtyP"

        except AssertionError:
            Problema1.fallo = False
            print("❌ Error en la función invertir_cadena.")
        except Exception as e:
            Problema1.fallo = False
            print(f"❌ Error: {e}")
        else:
            Problema1.fallo = True
            print("✅ Función correcta.")
