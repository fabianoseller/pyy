class Carro:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    # Getters
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_ano(self):
        return self.__ano

    # Setters
    def set_marca(self, nova_marca):
        self.__marca = nova_marca

    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    def set_ano(self, novo_ano):
        self.__ano = novo_ano

# Criando um objeto da classe Carro
carro = Carro("Toyota", "Corolla", 2022)

# Acessando e imprimindo a marca do carro
print("Marca do carro:", carro.get_marca())

# Alterando a marca do carro
carro.set_marca("Honda")

# Acessando e imprimindo o modelo do carro
print("Modelo do carro:", carro.get_modelo())

# Alterando o modelo do carro
carro.set_modelo("Civic")

# Acessando e imprimindo o ano de fabricação do carro
print("Ano de fabricação do carro:", carro.get_ano())

# Alterando o ano de fabricação do carro
carro.set_ano(2023)


# Neste código, definimos a classe Carro com os 
# atributos marca, modelo e ano, e implementamos 
# os métodos getters e setters para cada um deles.
# Depois, criamos uma instância dessa classe (carro)
# e realizamos as operações solicitadas: acessar/imprimir e alterar a marca, o modelo e o ano de fabricação do carro.