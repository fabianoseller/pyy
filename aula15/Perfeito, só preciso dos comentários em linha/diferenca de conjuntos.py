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
    
#3-*-*-*-*-*-*-*-*-


