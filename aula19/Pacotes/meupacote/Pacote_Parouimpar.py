# 4. Par ou ímpar
def par_ou_impar(num):
    if num % 2 == 0:
        print(f"{num} é um número par.")
        return True
    else:
        print(f"{num} é um número ímpar.")
        return False

# Exemplo de uso:
numero = 7
resultado = par_ou_impar(numero)