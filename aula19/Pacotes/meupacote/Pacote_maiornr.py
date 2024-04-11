# 2. Maior número
# 2. Maior número

def maior(x, y, z):
    max_valor = x
    if y > max_valor:
        max_valor = y
    if z > max_valor:
        max_valor = z
    return max_valor

def menor(x, y, z):
    min_valor = x
    if y < min_valor:
        min_valor = y
    if z < min_valor:
        min_valor = z
    return min_valor

def menu():
    x = int(input('Primeiro número: '))
    y = int(input('Segundo número: '))
    z = int(input('Terceiro número: '))
    print("Maior:", maior(x, y, z))
    print("Menor:", menor(x, y, z))

while True:
    menu()
