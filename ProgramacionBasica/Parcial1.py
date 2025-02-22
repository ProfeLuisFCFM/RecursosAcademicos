# Parcial1.py
from abc import ABC, abstractmethod

class ProblemaBase(ABC):
    """
    Clase base para todos los problemas. Define la estructura de `resolver()` y `check()`.
    """
    @abstractmethod
    def resolver(self, *args, **kwargs):
        """Método que el usuario debe implementar en cada problema."""
        pass

    @classmethod
    def check(cls):
        """Ejecuta los casos de prueba sin necesidad de instanciar la clase."""
        instancia = cls()
        for entrada, salida_esperada in instancia.casos_prueba():
            resultado = instancia.resolver(*entrada)
            if resultado == salida_esperada:
                print(f"✅ Correcto para entrada {entrada}")
            else:
                print(f"❌ Error para entrada {entrada}: Esperado {salida_esperada}, pero se obtuvo {resultado}")

    @staticmethod
    def casos_prueba():
        """Debe ser sobreescrito por cada problema para definir los casos de prueba."""
        return []

class Problema1(ProblemaBase):
    """Problema 1: Invertir una cadena."""
    
    def resolver(self, cadena):
        return cadena[::-1]
    
    @staticmethod
    def casos_prueba():
        return [
            (("hola",), "aloh"),
            (("Python",), "nohtyP"),
            (("12345",), "54321")
        ]

class Problema2(ProblemaBase):
    """Problema 2: Suma de una lista de números."""
    
    def resolver(self, numeros):
        return sum(numeros)
    
    @staticmethod
    def casos_prueba():
        return [
            (([1, 2, 3, 4, 5],), 15),
            (([10, -2, 8],), 16),
            (([],), 0)
        ]

class Problema3(ProblemaBase):
    """Problema 3: Determinar si un número es primo."""
    
    def resolver(self, numero):
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True
    
    @staticmethod
    def casos_prueba():
        return [
            ((2,), True),
            ((4,), False),
            ((17,), True),
            ((18,), False)
        ]

class Problema4(ProblemaBase):
    """Problema 4: Factorial de un número."""
    
    def resolver(self, n):
        if n == 0:
            return 1
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
    
    @staticmethod
    def casos_prueba():
        return [
            ((5,), 120),
            ((0,), 1),
            ((3,), 6)
        ]

class Problema5(ProblemaBase):
    """Problema 5: Encontrar el número mayor en una lista."""
    
    def resolver(self, numeros):
        return max(numeros)
    
    @staticmethod
    def casos_prueba():
        return [
            (([1, 2, 3, 4, 5],), 5),
            (([10, -2, 8],), 10),
            (([7, 7, 7],), 7)
        ]

class Problema6(ProblemaBase):
    """Problema 6: Contar las vocales en una cadena."""
    
    def resolver(self, cadena):
        return sum(1 for c in cadena.lower() if c in "aeiou")
    
    @staticmethod
    def casos_prueba():
        return [
            (("hola",), 2),
            (("Python",), 1),
            (("aeiou",), 5)
        ]
