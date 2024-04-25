# class ProdutoEletronico:
#     def __init__(self, codigo, nome, marca, modelo, preco, tipo):
#         self.codigo = codigo
#         self.nome = nome
#         self.marca = marca
#         self.modelo = modelo
#         selfpreco = preco
#         self.tipo = tipo
       
    
#     def garantia_estendida(self):
#         return self.garantia_estendida + self.aumentar_preco
    
#     def  garantia_estendida(self): FALTA CRIR OPÇÇÃO AQUI APRA VR COM FAZER "EM CONSTRUÇÃO" xx
    
#     def calcula_valor_totalavalor_Totalself, percentual):
#         self.preco_passagem -= self.preco_passagem * percentual / 100
    
#     def mostrar_informacoes(self):
#         print("Código:", self.codigo)
#         print("Nome:", self.nome)
#         print("Marca:", self.marca)
#         print("Modelo", self.modelo)
#         print("Preço:", self.preco)
#         print("Tipo:", self.tipo)
      

# 
class ProdutoEletronico:
    def __init__(self, codigo, nome, marca, modelo, preco, tipo):
        # Atributos privados
        self.__codigo = codigo
        self.__nome = nome
        self.__marca = marca
        self.__modelo = modelo
        self.__preco = preco
        self.__tipo = tipo
        self.__garantia_estendida = 300

    def aplicar_garantia_estendida(self, valor_extra):
        """
        Adiciona garantia estendida ao produto, aumentando o seu preço.
        :param valor_extra: Valor a ser adicionado ao preço do produto para a garantia estendida.
        """
        self.__garantia_estendida += valor_extra

    def calcular_valor_total(self):
        """
        Calcula o valor total do produto, considerando a garantia estendida, se aplicável.
        :return: Preço total do produto com garantia estendida.
        """
        return self.__preco + self.__garantia_estendida

    # Métodos adicionais para acessar os atributos de forma controlada podem ser úteis
    def get_informacoes(self):
        """
        Retorna as informações básicas do produto.
        """
        return (f"Código: {self.__codigo}, Nome: {self.__nome}, Marca: {self.__marca}, "
                f"Modelo: {self.__modelo}, Preço: {self.__preco}, Tipo: {self.__tipo}, "
                f"Garantia Estendida: {self.__garantia_estendida}")
        
        print(f"Garantia Estendida: {self.__garantia_estendida}")


# Exemplo de uso da classe
produto = ProdutoEletronico(codigo=1, nome="Computador", marca="ABC Tech", modelo="ABC123", preco=1500, tipo="Desktop")
print(produto.get_informacoes())
produto.aplicar_garantia_estendida(200*2)
print(f"Valor total com garantia: {produto.calcular_valor_total()}")


# Neste exemplo, a classe `ProdutoEletronico` tem métodos para 
# adicionar uma garantia estendida ao preço e calcular este valor total.
# Os métodos e atributos privados garantem que os dados não sejam acessados diretamente,
# aumentando a segurança e integridade do objeto. Além disso, um método para obter informações do
# produto foi incluído para facilitar o acesso controlado a esses dados.
