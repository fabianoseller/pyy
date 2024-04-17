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

    # Método para depositar dinheiro na conta
    def depositar(self, valor):
        self.__saldo += valor

if __name__ == "__main__":
    # Criando uma instância da classe ContaBancaria
    conta = ContaBancaria("João", 1000.0)

    # Acessando e imprimindo o nome do titular da conta
    print("Nome do titular:", conta.get_titular())

    # Alterando o nome do titular da conta
    conta.set_titular("Maria")

    # Acessando e imprimindo o saldo da conta
    print("Saldo da conta:", conta.get_saldo())

    # Depositando um valor na conta
    valor_deposito = 500.0
    conta.depositar(valor_deposito)

    # Acessando e imprimindo o novo saldo da conta
    print("Novo saldo da conta após depósito de", valor_deposito, ":", conta.get_saldo())
