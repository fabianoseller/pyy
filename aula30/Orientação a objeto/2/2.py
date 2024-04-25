from abc import ABC, abstractmethod

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
   
    return 3.1415 * self.raio ** 2

  def descrever(self):
   
    print(f"Figura: Círculo")
    print(f"Raio: {self.raio}")

# Criação de objeto
circulo1 = Circulo(5)

# Chamada de métodos
print("\nÁrea do círculo:", circulo1.calcular_area())
circulo1.descrever()