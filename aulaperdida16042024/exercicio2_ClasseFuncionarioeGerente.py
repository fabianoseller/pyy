class Funcionario:
    def __init__(self, nome, cargo, salario, data_admissao):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.data_admissao = data_admissao

    def calcular_pagamento(self):
        print(f"Salário a receber para {self.nome}: R${self.salario}")

    def apresentar_dados(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}, Salário: {self.salario}, Data de Admissão: {self.data_admissao}")


class Gerente(Funcionario):
    def __init__(self, nome, cargo, salario, data_admissao, bonus, area_gerenciada):
        super().__init__(nome, cargo, salario, data_admissao)
        self.bonus = bonus
        self.area_gerenciada = area_gerenciada

    def bonificar(self):
        print(f"Bonus adicionado ao salário de {self.nome}")

    def promover(self):
        print(f"{self.nome} foi promovido!")

    def apresentar_dados(self):
        super().apresentar_dados()
        print(f"Bônus: {self.bonus}, Área Gerenciada: {self.area_gerenciada}")


# Criando objetos
funcionario1 = Funcionario("João", "Analista", 5000, "01/01/2020")
gerente1 = Gerente("Maria", "Gerente de Vendas", 8000, "01/01/2018", 2000, "Vendas")

# Chamando métodos
funcionario1.calcular_pagamento()
funcionario1.apresentar_dados()
print("\n")
gerente1.calcular_pagamento()
gerente1.bonificar()
gerente1.promover()
gerente1.apresentar_dados()
