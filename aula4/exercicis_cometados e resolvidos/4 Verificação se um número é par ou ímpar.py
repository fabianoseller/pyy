#Cálculo da média de três notas:
  # Operadores aritméticos de soma (+) e divisão (/)

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
#Estas linhas solicitam ao usuário que digite as três notas e armazena os valores digitados nas variáveis nota1, nota2 e nota3.A função float() converte os valores digitados para números de ponto flutuante.
media = (nota1 + nota2 + nota3) / 3#Esta linha calcula a média das três notas utilizando a fórmula:A variável media armazena o resultado da fórmula.

print(f"A média das notas é: {media}")#Esta linha imprime a média das notas