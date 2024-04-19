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
