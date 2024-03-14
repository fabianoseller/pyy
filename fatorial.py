def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

try:
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 0:
        print("O fatorial não está definido para números negativos.")
    else:
        fatorial = calcular_fatorial(numero)
        print(f"O fatorial de {numero} é {fatorial}.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
