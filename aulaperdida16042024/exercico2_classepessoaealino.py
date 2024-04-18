class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def apresentar(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}")


class Aluno(Pessoa):
    def __init__(self, nome, idade, sexo, matricula):
        super().__init__(nome, idade, sexo)
        self.matricula = matricula

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, matricula):
        self.matricula = matricula


# Criando objetos
pessoa1 = Pessoa("João", 20, "Masculino")
aluno1 = Aluno("Maria", 22, "Feminino", "2023001")

# Chamando métodos
pessoa1.apresentar()
print("Matrícula do aluno:", aluno1.get_matricula())
