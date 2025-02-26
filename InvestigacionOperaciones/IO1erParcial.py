# Examen Práctico de Investigación de Operaciones
# Resolución de modelos matemáticos con scipy.optimize

import numpy as np
from scipy.optimize import linprog

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

# Problema 4: Cálculo del determinante de una matriz 4x4
def calcular_determinante(matriz):
    if matriz.shape != (4, 4):
        raise ValueError("La matriz debe ser de 4x4")
    return np.linalg.det(matriz)

if __name__ == "__main__":
    print("Ejecute las funciones para resolver los problemas.")
