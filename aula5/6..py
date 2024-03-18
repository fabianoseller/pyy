#6. Média de notas:
#Leia as notas de N alunos e calcule a média da turma usando while.

numero_alunos = int(input("Digite o número de alunos: "))#Esta linha pede ao usuário para digitar o número de alunos na turma.A função input() retorna uma string, então a convertemos para um número inteiro usando a função int().A variável numero_alunos armazena o número de alunos digitado pelo usuário.
soma_notas = 0#Esta linha define a variável soma_notas como 0.Essa variável será usada para armazenar a soma das notas de todos os alunos.

for i in range(numero_alunos):#Esta linha inicia um loop que será executado numero_alunos vezes.A variável i é usada para controlar a iteração do loop.
  nota = float(input(f"Digite a nota do aluno {i + 1}: "))#Dentro do loop, esta linha pede ao usuário para digitar a nota do aluno atual.A função f-string é usada para formatar a mensagem com o número do aluno.A função input() retorna uma string, então a convertemos para um número real usando a função float().A variável nota armazena a nota digitada pelo usuário.
  soma_notas += nota#Esta linha soma a nota do aluno atual à variável soma_notas.

media = soma_notas / numero_alunos#Esta linha calcula a média da turma dividindo a soma das notas pelo número de alunos.A variável media armazena a média calculada.
print(f"A média da turma é {media}")#Esta linha imprime a média da turma na tela.A função f-string é usada para formatar a mensagem com a variável media.
