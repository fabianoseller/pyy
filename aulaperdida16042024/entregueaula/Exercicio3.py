
class Aluno:
    def __init__(self, matricula, nome, curso):
        self.__matricula = matricula
        self.__nome = nome
        self.__curso = curso

    # Getters
    def get_matricula(self):
        return self.__matricula

    def get_nome(self):
        return self.__nome

    def get_curso(self):
        return self.__curso

    # Setters
    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_curso(self, novo_curso):
        self.__curso = novo_curso

# objeto da classe Aluno
aluno = Aluno(2024001, "João Silva", "Engenharia Civil")

# Acess e imp o número da matrícula do aluno
print("Matrícula do aluno:", aluno.get_matricula())

# Alt o num da matrícula do aluno
aluno.set_matricula(2024002)

# Acesso e impo o nome do aluno
print("Nome do aluno:", aluno.get_nome())

# Alt o nome do aluno
aluno.set_nome("Maria Oliveira")

# Acess e imprimindo o nome do curso do aluno
print("Curso do aluno:", aluno.get_curso())

# Alto o nome do curso do aluno
aluno.set_curso("Ciência da Computação")
