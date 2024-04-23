
class Funcionario(ABC):
    def __init__(self, nome, cargo, salario, folga):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.folga = folga
    
    @abstractmethod
    def calcular_pagamento(self):
        pass
    
    @abstractmethod
    def tirar_ferias(self):
        pass

class CLT(Funcionario):
    def calcular_pagamento(self):
        # Enetendimento para especificidades do metodo funcionários CLT
        pass
    
    def tirar_ferias(self):
        # Enetendimento para especificidades do metodo funcionários CLT
        pass

class PJ(Funcionario):
    def calcular_pagamento(self):
        # Enetendimento para especificidades do metodo funcionários PJ
        pass
    
    def tirar_ferias(self):
        # Enetendimento para especificidades do metodo funcionários PJ
        pass

class Freelancer(Funcionario):
    def calcular_pagamento(self):
        # Enetendimento para especificidades do metodo freelancers
        pass
    
    def tirar_ferias(self):
        # Enetendimento para especificidades do metodo freelancers
        pass
