import subprocess, sys, time
import numpy as np
import sympy as sp
from abc import ABC, abstractmethod
from scipy.optimize import linprog
from google.colab import files
from IPython.display import display
from PIL import Image as PILImage


def requisitos():
    libraries = [
        'numpy',
        'sympy',
        'qrcode',
        'Pillow'
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
    
    # Ahora importamos todas las librerías necesarias
    
    print("✅ Todas las librerías han sido importadas correctamente.")

requisitos()

def QR_Generator():
    import qrcode 
    espacio_usuario = get_ipython().user_ns

    try:
        Nombre = espacio_usuario["Nombre"]
        Matricula = espacio_usuario["Matricula"]
        Grupo = espacio_usuario["Grupo"]
    except KeyError as e:
        raise NameError(f"⚠️ La variable '{e.args[0]}' no está definida en el notebook. Asegúrate de ejecutarla antes.") 

    resultados = {}

    try:
        # Prueba para p1 (optimizar_sombreros)
        optimizar_sombreros = espacio_usuario["optimizar_sombreros"]
        try:
            # Definir los parámetros esperados para p1
            c = [-8, -5]  
            A = [[2, 1], [-1, 0], [0, -1]]  
            b = [350, -750, -600]
            bounds = [(0, None), (0, None)]  
            
            resultado_esperado = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs').x
            resultado_usuario = optimizar_sombreros()
            
            if all(abs(a - b) < 1e-5 for a, b in zip(resultado_usuario, resultado_esperado)):
                resultados["p1_optimizar_sombreros"] = True
            else:
                resultados["p1_optimizar_sombreros"] = False
        except Exception:
            resultados["p1_optimizar_sombreros"] = False

        # Prueba para p2 (optimizar_chemlabs)
        optimizar_chemlabs = espacio_usuario["optimizar_chemlabs"]
        try:
            # Definir los parámetros esperados para p2
            c = [-8.6, -15.4]  
            A = [[0.5, 0.5], [0.6, 0.4], [-1, 0], [0, -1]]  
            b = [210, 250, -60, -80]
            bounds = [(60, 200), (80, 300)]  
            
            resultado_esperado = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs').x
            resultado_usuario = optimizar_chemlabs()
            
            if all(abs(a - b) < 1e-5 for a, b in zip(resultado_usuario, resultado_esperado)):
                resultados["p2_optimizar_chemlabs"] = True
            else:
                resultados["p2_optimizar_chemlabs"] = False
        except Exception:
            resultados["p2_optimizar_chemlabs"] = False

        # Prueba para p3 (multiplicadores_lagrange_kkt)
        multiplicadores_lagrange_kkt = espacio_usuario["multiplicadores_lagrange_kkt"]
        try:
            # Definir los multiplicadores y las restricciones de p3
            x, y, lam1, lam2 = sp.symbols('x y lam1 lam2')
            f = x**2 + y**2
            g1 = x + y - 1
            g2 = x - y
            L = f - lam1 * g1 - lam2 * g2
            eq1 = sp.diff(L, x)
            eq2 = sp.diff(L, y)
            eq3 = sp.diff(L, lam1)
            eq4 = sp.diff(L, lam2)
            solucion_esperada = sp.solve([eq1, eq2, eq3, eq4], (x, y, lam1, lam2), dict=True)
            solucion_usuario = multiplicadores_lagrange_kkt()
            
            if solucion_usuario == solucion_esperada:
                resultados["p3_multiplicadores_lagrange_kkt"] = True
            else:
                resultados["p3_multiplicadores_lagrange_kkt"] = False
        except Exception:
            resultados["p3_multiplicadores_lagrange_kkt"] = False

        # Prueba para p4 (calcular_determinante)
        calcular_determinante = espacio_usuario["calcular_determinante"]
        try:
            # Crear una matriz aleatoria 4x4 para p4
            matriz = np.random.rand(4, 4)
            determinante_esperado = np.linalg.det(matriz)
            determinante_usuario = calcular_determinante(matriz)
            
            if abs(determinante_usuario - determinante_esperado) < 1e-5:
                resultados["p4_calcular_determinante"] = True
            else:
                resultados["p4_calcular_determinante"] = False
        except Exception:
            resultados["p4_calcular_determinante"] = False

    except KeyError as e:
        raise NameError(f"⚠️ La función '{e.args[0]}' no está definida en el notebook.")
    except Exception as e:
        raise RuntimeError(f"⚠️ Error en la ejecución de una función: {e}")

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
    img = PILImage.open(output_filename)
    display(img)

class p1(ABC):
    
    @abstractmethod
    def optimizar_sombreros(self):
        pass
    
    @staticmethod
    def check():
        try:
            espacio_usuario = get_ipython().user_ns
            if "optimizar_sombreros" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'optimizar_sombreros'.")
            
            funcion_usuario = espacio_usuario["optimizar_sombreros"]
            
            # Definir los parámetros esperados
            c = [-8, -5]  # Coeficientes de la función objetivo (maximizar utilidad)
            A = [[2, 1], [1, 0], [0, 1]]  # Restricciones
            b = [350, 750, 600]
            bounds = [(0, None), (0, None)]  # Variables no negativas
            
            # Resolver con scipy.optimize.linprog
            resultado_esperado = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs').x
            resultado_usuario = funcion_usuario()
            
            assert resultado_usuario is not None, "❌ La función no retorna un resultado."
            assert len(resultado_usuario) == len(resultado_esperado), "❌ El tamaño del resultado es incorrecto."
            assert all(abs(a - b) < 1e-5 for a, b in zip(resultado_usuario, resultado_esperado)), "❌ El resultado de la optimización no es correcto."
            
        except AssertionError as e:
            print(e)
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        else:
            print("✅ Función correcta.")
    
    @staticmethod
    def hint():
        print("Debes crear una función llamada 'optimizar_sombreros' que resuelva un problema de optimización lineal con 'linprog' de SciPy.")
        print("La función debe definir correctamente la función objetivo, las restricciones y los límites de las variables.")

class p2(ABC):
    
    @abstractmethod
    def optimizar_chemlabs(self):
        pass
    
    @staticmethod
    def check():
        try:
            espacio_usuario = get_ipython().user_ns
            if "optimizar_chemlabs" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'optimizar_chemlabs'.")
            
            funcion_usuario = espacio_usuario["optimizar_chemlabs"]
            
            # Definir los parámetros esperados
            c = [-8.6, -15.4]  # Coeficientes de la función objetivo
            A = [[0.5, 0.5], [0.6, 0.4], [-1, 0], [0, -1]]  # Restricciones
            b = [210, 250, -60, -80]
            bounds = [(60, 200), (80, 300)]  # Límites de variables
            
            # Resolver con scipy.optimize.linprog
            resultado_esperado = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs').x
            resultado_usuario = funcion_usuario()
            
            assert resultado_usuario is not None, "❌ La función no retorna un resultado."
            assert len(resultado_usuario) == len(resultado_esperado), "❌ El tamaño del resultado es incorrecto."
            assert all(abs(a - b) < 1e-5 for a, b in zip(resultado_usuario, resultado_esperado)), "❌ El resultado de la optimización no es correcto."
            
        except AssertionError as e:
            print(e)
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        else:
            print("✅ Función correcta.")
    
    @staticmethod
    def hint():
        print("Debes crear una función llamada 'optimizar_chemlabs' que resuelva un problema de optimización lineal con 'linprog' de SciPy.")
        print("La función debe definir correctamente la función objetivo, las restricciones y los límites de las variables.")

class p3(ABC):
    
    @abstractmethod
    def multiplicadores_lagrange_kkt(self):
        pass
    
    @staticmethod
    def check():
        try:
            espacio_usuario = get_ipython().user_ns
            if "multiplicadores_lagrange_kkt" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'multiplicadores_lagrange_kkt'.")
            
            funcion_usuario = espacio_usuario["multiplicadores_lagrange_kkt"]
            
            # Definir las variables y los multiplicadores
            x, y, lam1, lam2 = sp.symbols('x y lam1 lam2')
            
            # Función objetivo: f(x, y) = x^2 + y^2
            f = x**2 + y**2
            
            # Restricciones:
            g1 = x + y - 1
            g2 = x - y
            
            # Construir la función Lagrangiana
            L = f - lam1 * g1 - lam2 * g2
            
            # Calcular las derivadas parciales
            eq1 = sp.diff(L, x)    # ∂L/∂x = 0
            eq2 = sp.diff(L, y)    # ∂L/∂y = 0
            eq3 = sp.diff(L, lam1) # ∂L/∂lam1 = 0
            eq4 = sp.diff(L, lam2) # ∂L/∂lam2 = 0
            
            # Resolver el sistema de ecuaciones
            solucion_esperada = sp.solve([eq1, eq2, eq3, eq4], (x, y, lam1, lam2), dict=True)
            solucion_usuario = funcion_usuario()
            
            assert solucion_usuario == solucion_esperada, "❌ La solución obtenida no es correcta."
            
        except AssertionError as e:
            print(e)
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        else:
            print("✅ Función correcta.")
    
    @staticmethod
    def hint():
        print("Debes crear una función llamada 'multiplicadores_lagrange_kkt' que resuelva un sistema de ecuaciones basado en los multiplicadores de Lagrange.")
        print("Utiliza SymPy para definir las ecuaciones y resolverlas simbólicamente.")

class p4(ABC):
    
    @abstractmethod
    def calcular_determinante(self, matriz):
        pass
    
    @staticmethod
    def check():
        try:
            espacio_usuario = get_ipython().user_ns
            if "calcular_determinante" not in espacio_usuario:
                raise NameError("⚠️ No se encontró la función 'calcular_determinante'.")
            
            funcion_usuario = espacio_usuario["calcular_determinante"]
            
            # Crear una matriz aleatoria 4x4
            matriz = np.random.rand(4, 4)
            determinante_esperado = np.linalg.det(matriz)
            determinante_usuario = funcion_usuario(matriz)
            
            assert isinstance(determinante_usuario, (int, float, np.float64)), "❌ El resultado no es un número."
            assert abs(determinante_usuario - determinante_esperado) < 1e-5, "❌ El determinante calculado no es correcto."
            
        except AssertionError as e:
            print(e)
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        else:
            print("✅ Función correcta.")
    
    @staticmethod
    def hint():
        print("Debes crear una función llamada 'calcular_determinante' que reciba una matriz 4x4 y retorne su determinante usando NumPy.")

