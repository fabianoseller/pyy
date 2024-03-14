def fatorial(n):
    prod = 1
    for c in range(n, 0, -1):
        prod *= c
    return prod


num = int(input('Digite um número inteiro: '))

print(fatorial(num))