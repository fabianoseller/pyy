# # Neste exemplo, a classe Produto possui mét
# odos getters 
# e setters para os atributos nome e preco, além de um método aplicar_desconto para reduzir
#  o preço do produto com base em um desconto percentual fornecido.

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

    # Método para aplicar desconto no preço do produto
    def aplicar_desconto(self, desconto_percentual):
        desconto = self.__preco * (desconto_percentual / 100)
        self.__preco -= desconto

if __name__ == "__main__":
    # Criando uma instância da classe Produto
    produto = Produto("Camiseta", 50.0)

    # Acessando e imprimindo o nome do produto
    print("Nome do produto:", produto.get_nome())

    # Alterando o nome do produto
    produto.set_nome("Calça Jeans")

    # Acessando e imprimindo o preço do produto
    print("Preço do produto:", produto.get_preco())

    # Aplicando um desconto no preço do produto
    desconto_percentual = 10  # 10% de desconto
    produto.aplicar_desconto(desconto_percentual)

    # Acessando e imprimindo o novo preço do produto após o desconto
    print("Novo preço do produto após desconto de", desconto_percentual, "%:", produto.get_preco())
