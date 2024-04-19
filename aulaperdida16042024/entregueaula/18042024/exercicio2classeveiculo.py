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

    @abstractmethod
    def descrever(self):
        pass


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, numero_portas, tipo_cambio):
        super().__init__(marca, modelo, ano)
        self.cor = cor
        self.numero_portas = numero_portas
        self.tipo_cambio = tipo_cambio

    def ligar(self):
        print("Carro ligado.")

    def desligar(self):
        print("Carro desligado.")

    def acelerar(self):
        print("Carro acelerando.")

    def frear(self):
        print("Carro freando.")

    def descrever(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Cor: {self.cor}, Número de Portas: {self.numero_portas}, Tipo de Câmbio: {self.tipo_cambio}")


Aqui Criando objeto, para eu entender
carro1 = Carro("Toyota", "Corolla", 2022, "Preto", 4, "Automático")

Aqui Chamando métodos >> para eu entender
carro1.ligar()
carro1.acelerar()
carro1.frear()
carro1.descrever()
carro1.desligar()
