class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

  # Getter para nome
  def get_nome(self):
    return self.nome

  # Setter para nome
  def set_nome(self, novo_nome):
    self.nome = novo_nome

  # Getter para preço
  def get_preco(self):
    return self.preco

  # Setter para preço
  def set_preco(self, novo_preco):
    if novo_preco >= 0:
      self.preco = novo_preco
    else:
      print("Preço inválido. O preço não pode ser negativo.")

  # Método para aplicar desconto
  def aplicar_desconto(self, percentual_desconto):
    if percentual_desconto > 0 and percentual_desconto <= 100:
      desconto = self.preco * (percentual_desconto / 100)
      novo_preco = self.preco - desconto
      self.preco = novo_preco
      print(f"Desconto de {percentual_desconto}% aplicado com sucesso! Novo preço: R${novo_preco:.2f}")
    else:
      print("Percentual de desconto inválido. Deve ser um valor entre 0 e 100.")

# Criando um objeto da classe Produto
produto = Produto("Camisa", 50.00)

# Acessando e imprimindo o nome do produto
print(f"Nome do produto: {produto.get_nome()}")

# Alterando o nome do produto
produto.set_nome("Camiseta")

# Acessando e imprimindo o novo nome do produto
print(f"Novo nome do produto: {produto.get_nome()}")

# Acessando e imprimindo o preço do produto
print(f"Preço: R${produto.get_preco():.2f}")

# Aplicando desconto de 20%
produto.aplicar_desconto(20)

# Acessando e imprimindo o novo preço do produto
print(f"Novo preço: R${produto.get_preco():.2f}")