# "##################################Setters##################################")
#                 print("São métodos que modificam os valores dos atributos privados da classe.")
#                 print("Seguem a convenção de usar o prefixo set_ seguido pelo nome do atributo.")
#                 print("Recebem um argumento que representa o novo valor do atributo.")
#                 print("Não retornam nenhum valor.")
#                 print("Atualizam o valor do atributo correspondente com o valor recebido.")
#                 continuar_metodo_animal = input("Deseja printar o código abaixo sobre interação

#uma classe Aluno com os atributos matricula,
#nome e curso, e implementamos os métodos getters e setters
#para cada um deles. Em seguida, criamos uma
#instância dessa classe (aluno) e realizamos as
#operações solicitadas: acessar/imprimir e alterar a matrícula, o nome e o curso do aluno.

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

# Criando um objeto da classe Aluno
aluno = Aluno(2024001, "João Silva", "Engenharia Civil")

# Acessando e imprimindo o número da matrícula do aluno
print("Matrícula do aluno:", aluno.get_matricula())

# Alterando o número da matrícula do aluno
aluno.set_matricula(2024002)

# Acessando e imprimindo o nome do aluno
print("Nome do aluno:", aluno.get_nome())

# Alterando o nome do aluno
aluno.set_nome("Maria Oliveira")

# Acessando e imprimindo o nome do curso do aluno
print("Curso do aluno:", aluno.get_curso())

# Alterando o nome do curso do aluno
aluno.set_curso("Ciência da Computação")
