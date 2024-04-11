def verifica_palindromo_reversed(word):
    # Remove espaços e converte para minúsculas
    word = word.lower().replace(" ", "")
    
    # Verifica se a string original é igual à sua versão invertida
    if str(word) == "".join(reversed(word)):
        return True
    else:
        return False

# Exemplo de uso
entrada = input("Digite uma palavra ou frase: ")
if verifica_palindromo_reversed(entrada):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
