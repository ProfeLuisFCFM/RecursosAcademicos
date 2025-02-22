import os
import subprocess
import sys

# Lista de librerías que deseas instalar
libraries = [
    'wget',
    'pyqrcode'
]

# Función para instalar las librerías si no están ya instaladas
def requisitos():
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

# Llamamos a la función para instalar las librerías necesarias
#requisitos()

##### Funciones abstractas:


def invertir_cadena(cadena):
    pass  # Completa esta función




def p1_check():
    try: 
        assert invertir_cadena("hola") == "aloh"
        assert invertir_cadena("Python") == "nohtyP"
    except AssertionError:
        print("❌ La cadena no se invierte correctamente")
    else:
        print("✅ La cadena se invierte correctamente")
