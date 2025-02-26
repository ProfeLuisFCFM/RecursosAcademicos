import subprocess, sys
from abc import ABC, abstractmethod

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
            assert funcion_usuario(5) == 120
            assert funcion_usuario(0) == 1
            assert funcion_usuario(3) == 6
        except AssertionError:
            print("❌ Error en la función fibonacci.")
        except Exception as e:
            print(f"❌ Error: {e}")
        else:
            print("✅ Función correcta.")

    @staticmethod
    def hint():
        print("Debes generar una función llamada 'fibonacci', que reciba una variable int() y despues debes retornar el valor de la multiplicación de n * (n-1) * (n-2) * ... * (1). \n Por ejemplo: factorial de 3 -> 6 \n             factorial de 0 -> 1")





# Problema 4: Fibonacci
print("\n# Problema 4: Escribe una función que retorne los primeros N números de la serie Fibonacci.")
def fibonacci(n):
    pass  # Completa esta función

# Pruebas
assert fibonacci(5) == [0, 1, 1, 2, 3]
assert fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

# Problema 5: Palíndromos
print("\n# Problema 5: Escribe una función que determine si una palabra es un palíndromo.")
def es_palindromo(palabra):
    pass  # Completa esta función

# Pruebas
assert es_palindromo("oso") == True
assert es_palindromo("python") == False
assert es_palindromo("ana") == True


# Problema 6: Suma de dígitos
print("\n# Problema 6: Escribe una función que calcule la suma de los dígitos de un número entero positivo.")
def suma_digitos(numero):
    pass  # Completa esta función

# Pruebas
assert suma_digitos(123) == 6
assert suma_digitos(456) == 15
assert suma_digitos(789) == 24