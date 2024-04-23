#Verificar se um caractere está presente em uma string:
# Operador de membro "in"

caractere = input("Digite um caractere: ")#Esta linha solicita ao usuário que digite um caractere e armazena o valor digitado na variável "caractere".
string = "Exemplo de string"#Esta linha define a variável "string" com o valor "Exemplo de string".

if caractere in string:#Esta linha verifica se o caractere digitado pelo usuário está presente na string. Se o caractere estiver presente, o bloco de código dentro do if será executado.
  print(f"O caractere '{caractere}' está presente na string.")#Se o caractere estiver presente na string, esta linha imprime uma mensagem informando o usuário.
else:#Se o caractere não estiver presente na string, o bloco de código dentro do else será executado.
  print(f"O caractere '{caractere}' não está presente na string.")#Se o caractere não estiver presente na string, esta linha imprime uma mensagem informando o usuário.