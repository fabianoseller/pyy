class Pessoa:
    def __init__(self, nome, idade, sexo, clube):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.clube = clube

    def Apresentar(self,):
        return f"Nome: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}, Time: {self.clube}"

class Aluno(Pessoa):
    def __init__(self, nome, idade, sexo, matricula, clube):
        super().__init__(nome, idade, sexo,clube )
        self.matricula = matricula
    def set_matricula(self, matricula):
        self.matricula = matricula
    def get_matricula(self):
        return self.matricula
    
    # Print na'o permite porque nao reconhece, retorna "none"
    


 


# Criando objetos
pessoa1 = Pessoa("João", 20, "Masculino", "Futibas")
aluno1 = Aluno("Maria", 22, "Feminino", "2023001", "Nautico")



print("Matrícula do aluno:", aluno1.get_matricula(),pessoa1.Apresentar())
