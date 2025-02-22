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

# Función vacía o abstracta
def invertir_cadena(cadena):
    pass

# Función p1_check dentro de Parcial1.py que imprime el error si hay una excepción
def p1_check():
    try: 
        # Llamamos a la función invertir_cadena (que puede ser redefinida en el Notebook)
        assert invertir_cadena("hola") == "aloh"
        assert invertir_cadena("Python") == "nohtyP"
    except AssertionError as e:
        print("❌ Error: La cadena no se invierte correctamente")
        print(f"Detalle del error: {str(e)}")  # Imprime el detalle de la excepción
    else:
        print("✅ La cadena se invierte correctamente")
