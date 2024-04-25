from abc import ABC, abstractmethod

class Veiculo(ABC):
 

  def __init__(self, marca, modelo, ano):
    
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass

  @abstractmethod
  def acelerar(self):
    pass

  @abstractmethod
  def frear(self):
    pass

  def descrever(self):
   
    print(f"Marca: {self.marca}")
    print(f"Modelo: {self.modelo}")
    print(f"Ano: {self.ano}")

class Carro(Veiculo):
  

  def __init__(self, marca, modelo, ano, cor, numero_portas, tipo_cambio):
    
    super().__init__(marca, modelo, ano)
    self.cor = cor
    self.numero_portas = numero_portas
    self.tipo_cambio = tipo_cambio

  def ligar(self):
    
    print(f"Ligando o {self.marca} {self.modelo}...")

  def desligar(self):
    
    print(f"Desligando o {self.marca} {self.modelo}...")

  def acelerar(self):
    
    print(f"Acelerando o {self.marca} {self.modelo}...")

  def frear(self):
    
    print(f"Freando o {self.marca} {self.modelo}...")

  def descrever(self):
   
    super().descrever()
    print(f"Cor: {self.cor}")
    print(f"Número de Portas: {self.numero_portas}")
    print(f"Tipo de Câmbio: {self.tipo_cambio}")

# Criação de objeto
carro1 = Carro("Fiat", "Palio", 2020, "Branco", 4, "Automático")

# Chamada de métodos
print("\nCarro 1:")
carro1.ligar()
carro1.acelerar()
carro1.frear()
carro1.desligar()
carro1.descrever()