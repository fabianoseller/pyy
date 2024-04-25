
class ContaBancaria(ABC):
    def __init__(self, titular, saldo, taxa_juros):
        self.titular = titular
        self.saldo = saldo
        self.taxa_juros = taxa_juros
    
    @abstractmethod
    def depositar(self, valor):
        pass
    
    @abstractmethod
    def sacar(self, valor):
        pass
    
    @abstractmethod
    def calcular_juros(self):
        pass

class ContaCorrente(ContaBancaria):
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")
    
    def calcular_juros(self):
        # Não há juros na conta corrente
        pass

class ContaPoupanca(ContaBancaria):
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")
    
    def calcular_juros(self):
        self.saldo *= (1 + self.taxa_juros)

class ContaInvestimento(ContaBancaria):
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")
    
    def calcular_juros(self):
        # Implementação específica para contas de investimento
        pass
