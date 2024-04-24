class Carro:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  # Getter para marca
  def get_marca(self):
    return self.marca

  # Setter para marca
  def set_marca(self, nova_marca):
    self.marca = nova_marca

  # Getter para modelo
  def get_modelo(self):
    return self.modelo

  # Setter para modelo
  def set_modelo(self, novo_modelo):
    self.modelo = novo_modelo

  # Getter para ano
  def get_ano(self):
    return self.ano

  # Setter para ano
  def set_ano(self, novo_ano):
    if novo_ano > 0:
      self.ano = novo_ano
    else:
      print("Ano inválido. O ano deve ser um valor positivo.")

# Criando um objeto da classe Carro
carro = Carro("Fiat", "Uno", 2020)

# Acessando e imprimindo a marca do carro
print(f"Marca: {carro.get_marca()}")

# Alterando a marca do carro
carro.set_marca("Volkswagen")

# Acessando e imprimindo a nova marca do carro
print(f"Nova marca: {carro.get_marca()}")

# Acessando e imprimindo o modelo do carro
print(f"Modelo: {carro.get_modelo()}")

# Alterando o modelo do carro
carro.set_modelo("Gol")

# Acessando e imprimindo o novo modelo do carro
print(f"Novo modelo: {carro.get_modelo()}")

# Acessando e imprimindo o ano de fabricação do carro
print(f"Ano: {carro.get_ano()}")

# Alterando o ano de fabricação do carro
carro.set_ano(2023)

# Acessando e imprimindo o novo ano de fabricação do carro
print(f"Novo ano: {carro.get_ano()}")