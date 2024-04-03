
# 2. Interseção de conjuntos: Escreva um programa que encontre a interseção de dois conjuntos. Utilize for para iterar pelos 
# elementos e if para verificar a presença em ambos os conjuntos

conjunto_element={'do', 're', 'mi', 'si'}
conjunto_element2={'fa', 'so', 'la', 'si'}
conjunto_comum=set()
if conjunto_element != conjunto_element2:
    conjunto_comum = conjunto_element & conjunto_element2
    print(f'{conjunto_comum}')
else:
    print(f'Não contém.')
    
    #3. Escreva um programa que encontre a diferença entre dois conjuntos. Utilize for para iterar pelos 
# elementos e if para verificar a presença no primeiro conjunto e não no segundo.

conjunto_element1={1,6,8, 10, 5}
conjunto_element2={6, 7, 8, 9, 10}

conjunto_diferente=set()

conjunto_diferente = conjunto_element1.symmetric_difference(conjunto_element2)
if conjunto_diferente != set():
    print(f'{conjunto_diferente}')
else:
    print('Não há diferenças!')