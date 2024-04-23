from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    @abstractmethod
    def calcular_area(self):
        pass

class Quadrado(FiguraGeometrica):
    def calcular_area(self):
        return self.base * self.base

class Retangulo(FiguraGeometrica):
    def calcular_area(self):
        return self.base * self.altura

class Triangulo(FiguraGeometrica):
    def calcular_area(self):
        return (self.base * self.altura) / 2

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

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    
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

class Carro(Veiculo):
    def ligar(self):
        print("Carro ligado.")
    
    def desligar(self):
        print("Carro desligado.")
    
    def acelerar(self):
        print("Carro acelerando.")
    
    def frear(self):
        print("Carro freando.")

class Moto(Veiculo):
    def ligar(self):
        print("Moto ligada.")
    
    def desligar(self):
        print("Moto desligada.")
    
    def acelerar(self):
        print("Moto acelerando.")
    
    def frear(self):
        print("Moto freando.")

class Caminhao(Veiculo):
    def ligar(self):
        print("Caminhão ligado.")
    
    def desligar(self):
        print("Caminhão desligado.")
    
    def acelerar(self):
        print("Caminhão acelerando.")
    
    def frear(self):
        print("Caminhão freando.")

class Funcionario(ABC):
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    
    @abstractmethod
    def calcular_pagamento(self):
        pass
    
    @abstractmethod
    def tirar_ferias(self):
        pass

class CLT(Funcionario):
    def calcular_pagamento(self):
        # Implementação específica para funcionários CLT
        pass
    
    def tirar_ferias(self):
        # Implementação específica para funcionários CLT
        pass

class PJ(Funcionario):
    def calcular_pagamento(self):
        # Implementação específica para funcionários PJ
        pass
    
    def tirar_ferias(self):
        # Implementação específica para funcionários PJ
        pass

class Freelancer(Funcionario):
    def calcular_pagamento(self):
        # Implementação específica para freelancers
        pass
    
    def tirar_ferias(self):
        # Implementação específica para freelancers
        pass

class Jogo(ABC):
    def __init__(self, nome, genero, plataforma, classificacao_indicativa):
        self.nome = nome
        self.genero = genero
        self.plataforma = plataforma
        self.classificacao_indicativa = classificacao_indicativa
    
    @abstractmethod
    def iniciar(self):
        pass
    
    @abstractmethod
    def pausar(self):
        pass
    
    @abstractmethod
    def salvar_jogo(self):
        pass
    
    @abstractmethod
    def carregar_jogo(self):
        pass

class RPG(Jogo):
    def iniciar(self):
        print("Iniciando jogo de RPG.")
    
    def pausar(self):
        print("Jogo de RPG pausado.")
    
    def salvar_jogo(self):
        print("Salvando progresso do jogo de RPG.")
    
    def carregar_jogo(self):
        print("Carregando jogo de RPG.")

class Aventura(Jogo):
    def iniciar(self):
        print("Iniciando jogo de aventura.")
    
    def pausar(self):
        print("Jogo de aventura pausado.")
    
    def salvar_jogo(self):
        print("Salvando progresso do jogo de aventura.")
    
    def carregar_jogo(self):
        print("Carregando jogo de aventura.")

class Estrategia(Jogo):
    def iniciar(self):
        print("Iniciando jogo de estratégia.")
    
    def pausar(self):
        print("Jogo de estratégia pausado.")
    
    def salvar_jogo(self):
        print("Salvando progresso do jogo de estratégia.")
    
    def carregar_jogo(self):
        print("Carregando jogo de estratégia.")
