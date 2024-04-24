from datetime import date

class Funcionario:
  

  def __init__(self, nome, cargo, salario, data_admissao):
   
    self.nome = nome
    self.cargo = cargo
    self.salario = salario
    self.data_admissao = data_admissao

  def calcular_pagamento(self):
   
    return self.salario

  def apresentar_dados(self):
   
    print(f"Nome: {self.nome}")
    print(f"Cargo: {self.cargo}")
    print(f"Salário: R$ {self.salario:.2f}")
    print(f"Data de Admissão: {self.data_admissao}")

class Gerente(Funcionario):
 

  def __init__(self, nome, cargo, salario, data_admissao, bonus, area_gerenciada):
   
    super().__init__(nome, cargo, salario, data_admissao)
    if self.cargo != "Gerente":
      raise ValueError("Cargo de um gerente deve ser 'Gerente'")
    self.bonus = bonus
    self.area_gerenciada = area_gerenciada

  def calcular_pagamento(self):
   
    return self.salario + self.bonus

  def apresentar_dados(self):
    
    super().apresentar_dados()
    print(f"Bônus: R$ {self.bonus:.2f}")
    print(f"Área Gerenciada: {self.area_gerenciada}")

# Criação de objetos
funcionario1 = Funcionario("João Silva", "Analista de Dados", 2500.0, date(2020, 1, 1))
gerente1 = Gerente("Maria Oliveira", "Gerente", 3500.0, date(2018, 7, 23), 500.0, "TI")

# Apresentação dos dados
print("\nFuncionário 1:")
funcionario1.apresentar_dados()

print("\nGerente 1:")
gerente1.apresentar_dados()