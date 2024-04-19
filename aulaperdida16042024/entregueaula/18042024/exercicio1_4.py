class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor


    # Getters
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_ano(self):
        return self.__ano

    def get_cor(self):
        return self.__cor


    # Setters
    def set_marca(self, nova_marca):
        self.__marca = nova_marca

    def set_modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    def set_ano(self, novo_ano):
        self.__ano = novo_ano

    def set_cor(self, novo_cor):
        self.__cor = novo_cor


carro = Carro("Toyota", "Corolla", 2022, "Vermelho")
print("Marca do carro:", carro.get_marca())

carro.set_marca("Honda")
print("Modelo do carro:", carro.get_modelo())

carro.set_modelo("Civic")
print("Ano de fabricação do carro:", carro.get_ano())
carro.set_ano(2023)

carro.set_cor("Preto")
print("Cor do carro:", carro.get_cor())
carro.set_cor("Vermelho")


