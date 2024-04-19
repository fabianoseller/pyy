from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def descrever(self):
        pass


class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

    def descrever(self):
        print(f"Círculo com raio {self.raio}")


# Criando objeto do circulo1
circulo1 = Circulo(5)

# Chamando métodos
print("Área do círculo:", circulo1.calcular_area())
circulo1.descrever()
