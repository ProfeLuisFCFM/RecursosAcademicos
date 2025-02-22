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


class problem1(ABC):
    @abstractmethod
    def invertir_cadena(self,cadena):
        pass

    def check(self):
        if self.invertir_cadena("hola") != "aloh":
            print("❌ Error: La cadena 'hola' no se invierte correctamente")
            print(f"Resultado: {self.invertir_cadena('hola')}")
        
        elif self.invertir_cadena("Python") != "nohtyP":
            print("❌ Error: La cadena 'Python' no se invierte correctamente")
            print(f"Resultado: {self.invertir_cadena('Python')}")
        
        else:
            print("✅ La cadena se invierte correctamente")
