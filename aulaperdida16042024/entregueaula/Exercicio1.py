

class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    # Getters
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    # Setters
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_preco(self, novo_preco):
        self.__preco = novo_preco

    # Aplicar desconto no preço do produto
    def aplicar_desconto(self, desconto_percentual):
        desconto = self.__preco * (desconto_percentual / 100)
        self.__preco -= desconto

if __name__ == "__main__":
    produto = Produto("Camiseta", 50.0)

    print("Nome do produto:", produto.get_nome())
    produto.set_nome("Calça Jeans")
    print("Preço do produto:", produto.get_preco())

    desconto_percentual = 10  # 10% de desconto
    produto.aplicar_desconto(desconto_percentual)

    # Acessando e imprimindo o novo preço do produto após o desconto
    print("Novo preço do produto após desconto de", desconto_percentual, "%:", produto.get_preco())
