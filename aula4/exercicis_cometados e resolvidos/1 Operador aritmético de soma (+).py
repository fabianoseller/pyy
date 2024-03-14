#Operador aritmético de soma (+)

num1 = int(input("Digite o primeiro número: "))#Esta linha solicita ao usuário que digite o primeiro número e armazena o valor digitado na variável num1.A função int() converte o valor digitado para um número inteiro.
num2 = int(input("Digite o segundo número: "))#Esta linha solicita ao usuário que digite o segundo número e armazena o valor digitado na variável num2.A função int() converte o valor digitado para um número inteiro.

soma = num1 + num2#Esta linha soma os valores das variáveis num1 e num2 e armazena o resultado na variável soma.

print(f"A soma dos números é: {soma}") #f-strings são uma maneira mais moderna de formatar strings em Python.Elas permitem que você inclua expressões dentro da string.As expressões são avaliadas e o resultado é inserido na string.A expressão dentro da f-string é {soma}.Esta expressão é avaliada e o valor da variável soma é inserido na string.