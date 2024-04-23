palavra_secreta = "banana"
palavra_com_acertos = "_" * len(palavra_secreta)
letras_usadas = ""
acertos = 0
erros = 0
numero_de_tentativa = int(len(palavra_secreta))

while erros < numero_de_tentativa and acertos < len(palavra_secreta):
    print(f"Palavra: {palavra_com_acertos}")
    print(f"Letras usadas: {letras_usadas}")

    letra = input("Digite uma letra: ")
    if letra in letras_usadas:
        print("Essa letra já foi utilizada.")
        continue

    letras_usadas += letra
    
    if letra in palavra_secreta:
        acertos += 1
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_com_acertos = palavra_com_acertos[:i] + letra + palavra_com_acertos[i + 1:]
                if palavra_com_acertos==palavra_secreta:
                    acertos = len(palavra_secreta)
                    break
                
                    
    else:
        erros += 1
        if erros==numero_de_tentativa:
            print(f"Você perdeu! A palavra era {palavra_secreta}")
            break


if acertos == len(palavra_secreta):
    print(f"Você venceu! A palavra era {palavra_secreta}")
