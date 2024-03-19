def inverter_tupla(tupla):
    # Usando slicing para inverter a ordem dos elementos da tupla
    tupla_invertida = tupla[::-1]
    return tupla_invertida

# Exemplo de uso
minha_tupla = (1, 2, 3, 4, 5)
tupla_invertida = inverter_tupla(minha_tupla)
print("Tupla original:", minha_tupla)
print("Tupla invertida:", tupla_invertida)
