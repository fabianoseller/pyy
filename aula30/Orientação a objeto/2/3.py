class ContaBancaria:
 

  def __init__(self, titular, saldo, taxa_juros):
   
    self.titular = titular
    self.saldo = saldo
    self.taxa_juros = taxa_juros

  def depositar(self, valor):
   
    if valor > 0:
      self.saldo += valor
      print(f"Depósito de {valor:.2f} realizado com sucesso!")
    else:
      print("Valor inválido para depósito.")

  def sacar(self, valor):
    
    if valor > 0 and valor <= self.saldo:
      self.saldo -= valor
      print(f"Saque de {valor:.2f} realizado com sucesso!")
    else:
      print("Saldo insuficiente ou valor inválido para saque.")

  def calcular_rendimento(self):
   
    return self.saldo * self.taxa_juros / 100

  def apresentar_saldo(self):
   
    print(f"Saldo: {self.saldo:.2f}")

class ContaPoupanca(ContaBancaria):
 
  def __init__(self, titular, saldo, taxa_juros, rendimento_mensal=0):

    super().__init__(titular, saldo, taxa_juros)
    self.rendimento_mensal = rendimento_mensal

  def calcular_rendimento(self):
  
    self.rendimento_mensal += super().calcular_rendimento()
    return self.rendimento_mensal

  def apresentar_saldo(self):
   
    super().apresentar_saldo()
    print(f"Rendimento mensal: {self.rendimento_mensal:.2f}")

# Criação de objetos
conta1 = ContaBancaria("João Silva", 1000, 0.01)
conta_poupanca1 = ContaPoupanca("Maria Oliveira", 500, 0.02)

# Chamada de métodos
print("\nConta Bancária:")
conta1.depositar(200)
conta1.sacar(150)
conta1.apresentar_saldo()

print("\nConta Poupança:")
conta_poupanca1.depositar(300)
conta_poupanca1.calcular_rendimento()
conta_poupanca1.sacar(100)
conta_poupanca1.apresentar_saldo()