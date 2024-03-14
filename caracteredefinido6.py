def verificar_caractere(string, caractere):
    if caractere in string:
        return f"O caractere '{caractere}' está presente na string."
    else:
        return f"O caractere '{caractere}' não foi encontrado na string."

try:
    string = input("Digite uma string: ")
    caractere = "6"  # Caractere definido como "6"

    resultado = verificar_caractere(string, caractere)
    print(resultado)
except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
