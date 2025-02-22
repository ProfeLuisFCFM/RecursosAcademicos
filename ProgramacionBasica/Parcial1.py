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

class p1(ABC):

    @abstractmethod
    def invertir_cadena(self, cadena):
        pass

    @staticmethod
    def check():
        try:
            espacio_usuario = get_ipython().user_ns
            if "invertir_cadena" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'invertir_cadena'.")
            funcion_usuario = espacio_usuario["invertir_cadena"]
            assert funcion_usuario("hola") == "aloh"
            assert funcion_usuario("Python") == "nohtyP"
        except AssertionError:
            p1.fallo = False
            print("❌ Error en la función invertir_cadena.")
        except Exception as e:
            p1.fallo = False
            print(f"❌ Error: {e}")
        else:
            p1.fallo = True
            print("✅ Función correcta.")

    @staticmethod
    def hint():
        print("Debes generar una función llamada 'invertir_cadena', que reciba una variable str() y despues la inviertas. \n Por ejemplo: 'problema1' -> '1amelborp'")
