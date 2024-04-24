class ContaBancaria:
  def __init__(self, titular, saldo):
    self.titular = titular
    self.saldo = saldo

  # Getter para titular
  def get_titular(self):
    return self.titular

  # Setter para titular
  def set_titular(self, novo_titular):
    self.titular = novo_titular

  # Getter para saldo
  def get_saldo(self):
    return self.saldo

  # Setter para saldo
  def set_saldo(self, novo_saldo):
    self.saldo = novo_saldo

  # Método para depositar valor
  def depositar(self, valor):
    if valor > 0:
      self.saldo += valor
      print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
      print("Valor inválido para depósito.")

  # Método para imprimir extrato
  def imprimir_extrato(self):
    print(f"Titular: {self.titular}")
    print(f"Saldo: R${self.saldo:.2f}")

# Criando um objeto da classe ContaBancaria
conta = ContaBancaria("João Silva", 1000.00)

# Acessando e imprimindo o nome do titular
print(f"Nome do titular: {conta.get_titular()}")

# Alterando o nome do titular
conta.set_titular("Maria Oliveira")

# Acessando e imprimindo o novo nome do titular
print(f"Novo nome do titular: {conta.get_titular()}")

# Acessando e imprimindo o saldo
print(f"Saldo: R${conta.get_saldo():.2f}")

# Depositando R$200,00
conta.depositar(200.00)

# Acessando e imprimindo o novo saldo
print(f"Novo saldo: R${conta.get_saldo():.2f}")

# Imprimindo extrato completo
conta.imprimir_extrato()