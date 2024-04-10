# 1. Calculadora básica
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

# 2. Maior número
def maior_numero(a, b):
    return max(a, b)

def media(a, b, c):
    return (a + b + c) / 3

# Exemplo de uso
resultado = media(10, 257, 13)
return (a + b + c) / 3
print("A média é:", resultado)

# 4. Par ou ímpar
def par_ou_impar(num):
    return num % 2 == 0

# 5. Tabuada
def tabuada(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# 6. Fatorial
def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)

# 7. Área de um triângulo
def area_triangulo(base, altura):
    return (base * altura) / 2

# 8. Palíndromo
def eh_palindromo(s):
    s = s.lower()
    return s == s[::-1]

# 9. Contador de vogais
def contador_vogais(s):
    vogais = 'aeiouAEIOU'
    return sum(1 for char in s if char in vogais)

# 10. Inverter string
def inverter_string(s):
    return s[::-1]
print(soma(5, 3))  # Saída: 8
print(maior_numero(10, 7))  # Saída: 10
print(media(4, 5, 6))  # Saída: 5.0
print(par_ou_impar(7))  # Saída: False
tabuada(7)  # Imprime a tabuada do 7
print(fatorial(5))  # Saída: 120
print(area_triangulo(3, 4))  # Saída: 6.0
print(eh_palindromo("ovo"))  # Saída: True
print(contador_vogais("Hello World"))  # Saída: 3
print(inverter_string("Hello"))  # Saída: "olleH"