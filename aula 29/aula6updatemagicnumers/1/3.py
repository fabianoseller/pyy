class Aluno:
  def __init__(self, matricula, nome, curso):
    self.matricula = matricula
    self.nome = nome
    self.curso = curso

  # Getter para matricula
  def get_matricula(self):
    return self.matricula

  # Setter para matricula
  def set_matricula(self, nova_matricula):
    self.matricula = nova_matricula

  # Getter para nome
  def get_nome(self):
    return self.nome

  # Setter para nome
  def set_nome(self, novo_nome):
    self.nome = novo_nome

  # Getter para curso
  def get_curso(self):
    return self.curso

  # Setter para curso
  def set_curso(self, novo_curso):
    self.curso = novo_curso

# Criando um objeto da classe Aluno
aluno = Aluno(12345, "João Silva", "Ciência da Computação")

# Acessando e imprimindo o número da matrícula
print(f"Número da matrícula: {aluno.get_matricula()}")

# Alterando o número da matrícula
aluno.set_matricula(98765)

# Acessando e imprimindo o novo número da matrícula
print(f"Novo número da matrícula: {aluno.get_matricula()}")

# Acessando e imprimindo o nome do aluno
print(f"Nome: {aluno.get_nome()}")

# Alterando o nome do aluno
aluno.set_nome("Maria Oliveira")

# Acessando e imprimindo o novo nome do aluno
print(f"Novo nome: {aluno.get_nome()}")

# Acessando e imprimindo o nome do curso
print(f"Curso: {aluno.get_curso()}")

# Alterando o nome do curso
aluno.set_curso("Engenharia Elétrica")

# Acessando e imprimindo o novo nome do curso
print(f"Novo curso: {aluno.get_curso()}")