aluno1 = {
    "nome": "João Silva",
    "idade": 20,
    "curso": "Ciência da Computação",
    "matricula": 123456
}

aluno2 = {
    "nome": "Maria Oliveira",
    "idade": 22,
    "curso": "Engenharia Elétrica",
    "matricula": 654321
}

if aluno1["nome"] == aluno2["nome"] and aluno1["idade"] == aluno2["idade"]:
    print("Os alunos possuem o mesmo nome e idade.")
else:
    print("Os alunos possuem nomes ou idades diferentes.")