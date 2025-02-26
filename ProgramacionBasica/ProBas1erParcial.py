import subprocess, sys, time, pyqrcode
from abc import ABC, abstractmethod
from google.colab import files

def requisitos():
    libraries = [
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
    print("✅ Verificación de requisitos completada.")

requisitos()


def QR_Generator():
    resultados = {}
    examen = {
        "datos_alumno": {
            "nombre": Nombre,
            "matricula": Matricula,
            "grupo": Grupo
        },
        "respuestas": resultados,
        "fecha": int(time.time())
    }
    qr = qrcode.make(examen)
    output_filename = "qr_resultados.png"
    qr.save(output_filename)
    print(f"Código QR generado y guardado como {output_filename}")
    files.download('qr_resultados.png')



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
            print("❌ Error en la función invertir_cadena.")
        except Exception as e:
            print(f"❌ Error: {e}")
        else:
            print("✅ Función correcta.")

    @staticmethod
    def hint():
        print("Debes generar una función llamada 'invertir_cadena', que reciba una variable str() y despues debes invertir el orden de impresión. \n Por ejemplo: 'problema1' -> '1amelborp'")

class p2(ABC):

    @abstractmethod
    def es_primo(self, cadena):
        pass

    @staticmethod
    def check():
        try:
            espacio_usuario = get_ipython().user_ns
            if "es_primo" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'es_primo'.")
            funcion_usuario = espacio_usuario["es_primo"]
            assert funcion_usuario(2) == True
            assert funcion_usuario(4) == False
            assert funcion_usuario(17) == True
        except AssertionError:
            print("❌ Error en la función es_primo.")
        except Exception as e:
            print(f"❌ Error: {e}")
        else:
            print("✅ Función correcta.")

    @staticmethod
    def hint():
        print("Debes generar una función llamada 'es_primo', que reciba una variable int() y despues debes retornar True si es primo o False si no lo es. \n Por ejemplo: 7 es primo \n             9 no es primo")

class p3(ABC):

    @abstractmethod
    def factorial(self, n):
        pass

    @staticmethod
    def check():
        try:
            espacio_usuario = get_ipython().user_ns
            if "factorial" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'factorial'.")
            funcion_usuario = espacio_usuario["factorial"]
            assert funcion_usuario(5) == 120
            assert funcion_usuario(0) == 1
            assert funcion_usuario(3) == 6
        except AssertionError:
            print("❌ Error en la función factorial.")
        except Exception as e:
            print(f"❌ Error: {e}")
        else:
            print("✅ Función correcta.")

    @staticmethod
    def hint():
        print("Debes generar una función llamada 'factorial', que reciba una variable int() y despues debes retornar el valor de la multiplicación de n * (n-1) * (n-2) * ... * (1). \n Por ejemplo: factorial de 3 -> 6 \n             factorial de 0 -> 1")

class p4(ABC):

    @abstractmethod
    def fibonacci(self, n):
        pass

    @staticmethod
    def check():
        try:
            espacio_usuario = get_ipython().user_ns
            if "fibonacci" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'fibonacci'.")
            funcion_usuario = espacio_usuario["fibonacci"]
            assert funcion_usuario(5) == [0, 1, 1, 2, 3]
            assert funcion_usuario(7) == [0, 1, 1, 2, 3, 5, 8]
        except AssertionError:
            print("❌ Error en la función fibonacci.")
        except Exception as e:
            print(f"❌ Error: {e}")
        else:
            print("✅ Función correcta.")

    @staticmethod
    def hint():
        print("Debes generar una función llamada 'fibonacci', que retorne los primeros N números de la serie Fibonacci.")

class p5(ABC):

    @abstractmethod
    def es_palindromo(self, palabra):
        pass

    @staticmethod
    def check():
        try:
            espacio_usuario = get_ipython().user_ns
            if "es_palindromo" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'es_palindromo'.")
            funcion_usuario = espacio_usuario["es_palindromo"]
            assert funcion_usuario("oso") == True
            assert funcion_usuario("python") == False
            assert funcion_usuario("ana") == True
        except AssertionError:
            print("❌ Error en la función es_palindromo.")
        except Exception as e:
            print(f"❌ Error: {e}")
        else:
            print("✅ Función correcta.")

    @staticmethod
    def hint():
        print("Debes generar una función llamada 'es_palindromo', que retorne True si una palabra es igual al revés.")

class p6(ABC):

    @abstractmethod
    def suma_digitos(self, numero):
        pass

    @staticmethod
    def check():
        try:
            espacio_usuario = get_ipython().user_ns
            if "suma_digitos" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'suma_digitos'.")
            funcion_usuario = espacio_usuario["suma_digitos"]
            assert funcion_usuario(123) == 6
            assert funcion_usuario(456) == 15
            assert funcion_usuario(789) == 24
        except AssertionError:
            print("❌ Error en la función suma_digitos.")
        except Exception as e:
            print(f"❌ Error: {e}")
        else:
            print("✅ Función correcta.")

    @staticmethod
    def hint():
        print("Debes generar una función llamada 'suma_digitos', que sume todos los dígitos de un número entero positivo.")
