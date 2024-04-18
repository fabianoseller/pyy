class ContaBancaria:
    def __init__(self, titular, saldo=0, taxa_juros=0.0):
        self.titular = titular
        self.saldo = saldo
        self.taxa_juros = taxa_juros

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            print("Saldo insuficiente.")
            return False

    def calcular_rendimento(self):
        return self.saldo * (self.taxa_juros / 100)

    def apresentar_saldo(self):
        print(f"Saldo atual: {self.saldo}")


class ContaPoupanca(ContaBancaria):
    def __init__(self, titular, saldo=0, taxa_juros=0.0, rendimento_mensal=0.0):
        super().__init__(titular, saldo, taxa_juros)
        self.rendimento_mensal = rendimento_mensal

    def calcular_rendimento(self):
        return super().calcular_rendimento() + self.rendimento_mensal


# Criando objetos
conta1 = ContaBancaria("João", 1000, 1.5)
conta_poupanca1 = ContaPoupanca("Maria", 2000, 2.0, 50)

# Chamando métodos
conta1.apresentar_saldo()
conta1.depositar(500)
conta1.apresentar_saldo()
conta_poupanca1.apresentar_saldo()
print("Rendimento mensal da conta poupança:", conta_poupanca1.calcular_rendimento())
