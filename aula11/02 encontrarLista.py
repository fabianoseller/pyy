#texto exercicio 1


 #texto exercicio 2
lista = []
maior = 0
menor = 0 
 

for exemplo in range(5):
    lista.append(int(input(f"Digite o valor para a posição {exemplo}: ")))
    if exemplo == 0:
        maior = menor = lista[exemplo]
    else:
        if lista[exemplo] > maior: 
            maior = lista[exemplo]
        if lista[exemplo] < menor:
            menor = lista[exemplo]
 

 

print(f'Valores digitados: {lista}')

print()
print(f'O maior valor digitado foi {maior}')
print()
print(f'O menor valor digitado foi {menor}')
