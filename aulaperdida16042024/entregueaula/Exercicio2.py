class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    # Getters
    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    # Setters
    def set_titular(self, novo_titular):
        self.__titular = novo_titular

    def set_saldo(self, novo_saldo):
        self.__saldo = novo_saldo
    def depositar(self, valor):
        self.__saldo += valor

if __name__ == "__main__":
    conta = ContaBancaria("João", 7000.0)
    print("Nome do titular:", conta.get_titular())
    conta.set_titular("Maria")
    print("Saldo da conta:", conta.get_saldo())
    valor_deposito = 700.0
    conta.depositar(valor_deposito)
    print("Novo saldo da conta após depósito de", valor_deposito, ":", conta.get_saldo())
