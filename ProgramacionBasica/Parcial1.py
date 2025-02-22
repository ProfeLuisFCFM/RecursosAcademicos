import subprocess
import sys

libraries = [
    'wget',
    'pyqrcode'
]

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


# Función vacía o abstracta
def invertir_cadena(cadena):
    pass


# Función de revisión
def p1_check():
    if invertir_cadena("hola") != "aloh":
        print("❌ Error: La cadena 'hola' no se invierte correctamente")
        print(f"Resultado: {invertir_cadena('hola')}")
    
    elif invertir_cadena("Python") != "nohtyP":
        print("❌ Error: La cadena 'Python' no se invierte correctamente")
        print(f"Resultado: {invertir_cadena('Python')}")
    
    else:
        print("✅ La cadena se invierte correctamente")
