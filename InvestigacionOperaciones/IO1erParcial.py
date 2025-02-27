# Examen Práctico de Investigación de Operaciones
# Resolución de modelos matemáticos con scipy.optimize

import numpy as np
from scipy.optimize import linprog
import sympy as sp

# Problema 1: Producción de sombreros en Wild West
def optimizar_sombreros():
    c = [-8, -5]  # Maximizar utilidad (se multiplica por -1 para linprog)
    A = [[2, 1], [-1, 0], [0, -1]]  # Restricciones de mano de obra y mercado
    b = [350, -750, -600]
    bounds = [(0, None), (0, None)]  # No negativos
    resultado = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    print("Optimización de producción de sombreros:", resultado.x)

# Problema 2: Producción óptima de soluciones de limpieza
def optimizar_chemlabs():
    c = [-8.6, -15.4]
    A = [[0.5, 0.5], [0.6, 0.4], [-1, 0], [0, -1]]
    b = [210, 250, -60, -80]
    bounds = [(60, 200), (80, 300)]
    resultado = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    print("Producción óptima de soluciones A y B:", resultado.x)

# Problema 3: Multiplicadores de Lagrange y KKT (teórico, resolver aparte)
def multiplicadores_lagrange_kkt():
    # Definir las variables y los multiplicadores
    x, y, lam1, lam2 = sp.symbols('x y lam1 lam2')
    
    # Función objetivo: f(x, y) = x^2 + y^2
    f = x**2 + y**2
    
    # Restricciones:
    # g1: x + y - 1 = 0
    # g2: x - y = 0
    g1 = x + y - 1
    g2 = x - y
    
    # Construir la función Lagrangiana:
    # L(x, y, lam1, lam2) = f(x, y) - lam1*g1 - lam2*g2
    L = f - lam1 * g1 - lam2 * g2
    
    # Calcular las derivadas parciales (condiciones de primer orden)
    eq1 = sp.diff(L, x)    # ∂L/∂x = 0
    eq2 = sp.diff(L, y)    # ∂L/∂y = 0
    eq3 = sp.diff(L, lam1) # ∂L/∂lam1 = 0  (la restricción g1)
    eq4 = sp.diff(L, lam2) # ∂L/∂lam2 = 0  (la restricción g2)
    
    # Resolver el sistema de ecuaciones
    solucion = sp.solve([eq1, eq2, eq3, eq4], (x, y, lam1, lam2), dict=True)
    return solucion


# Problema 4: Cálculo del determinante de una matriz 4x4
def calcular_determinante(matriz):
    if matriz.shape != (4, 4):
        raise ValueError("La matriz debe ser de 4x4")
    return np.linalg.det(matriz)

if __name__ == "__main__":
    print("Ejecute las funciones para resolver los problemas.")
