
class Pessoa:
 
  def __init__(self, nome, idade, sexo):
   
    self.nome = nome
    self.idade = idade
    self.sexo = sexo

  def get_nome(self):
  
    return self.nome

  def set_nome(self, novo_nome):
   
    self.nome = novo_nome

  def get_idade(self):
    
    return self.idade

  def set_idade(self, nova_idade):
   
    self.idade = nova_idade

  def get_sexo(self):
    
    return self.sexo

  def set_sexo(self, novo_sexo):
    
    self.sexo = novo_sexo

  def apresentar(self):
   
    print(f"Nome: {self.get_nome()}")
    print(f"Idade: {self.get_idade()}")
    print(f"Sexo: {self.get_sexo()}")

class Aluno(Pessoa):


  def __init__(self, nome, idade, sexo, matricula):
   
    super().__init__(nome, idade, sexo)
    self.matricula = matricula

  def get_matricula(self):
   
    return self.matricula

  def set_matricula(self, nova_matricula):
    
    self.matricula = nova_matricula

  def apresentar(self):
   
    super().apresentar()
    print(f"Matrícula: {self.get_matricula()}")

# Criação de objetos
pessoa1 = Pessoa("João Silva", 30, "Masculino")
aluno1 = Aluno("Maria Oliveira", 25, "Feminino", "12345")

# Chamada de métodos
print("Pessoa 1:")
pessoa1.apresentar()

print("\nAluno 1:")
aluno1.apresentar()

aluno1.set_matricula("54321")
print("\nNova matrícula do aluno 1:", aluno1.get_matricula())