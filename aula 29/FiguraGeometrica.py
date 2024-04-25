from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    @abstractmethod
    def calcular_area(self):
        pass

class Quadrado(FiguraGeometrica):
    def calcular_area(self):
        return self.base * self.base

class Retangulo(FiguraGeometrica):
    def calcular_area(self):
        return self.base * self.altura

class Triangulo(FiguraGeometrica):
    def calcular_area(self):
        return (self.base * self.altura) / 2
