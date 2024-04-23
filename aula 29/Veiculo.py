
class Veiculo(ABC):
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
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

class Carro(Veiculo):
    def ligar(self):
        print("Carro ligado.")
    
    def desligar(self):
        print("Carro desligado.")
    
    def acelerar(self):
        print("Carro acelerando.")
    
    def frear(self):
        print("Carro freando.")

class Moto(Veiculo):
    def ligar(self):
        print("Moto ligada.")
    
    def desligar(self):
        print("Moto desligada.")
    
    def acelerar(self):
        print("Moto acelerando.")
    
    def frear(self):
        print("Moto freando.")

class Caminhao(Veiculo):
    def ligar(self):
        print("Caminhão ligado.")
    
    def desligar(self):
        print("Caminhão desligado.")
    
    def acelerar(self):
        print("Caminhão acelerando.")
    
    def frear(self):
        print("Caminhão freando.")
