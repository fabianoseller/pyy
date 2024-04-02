conjunto = {1, 2, 2, 3, 3, 4, 5, 6, 6, 6, 6, 6, 6, 6}
sem_duplicados = set()
for elemento in conjunto:
    if elemento not in sem_duplicados:
        sem_duplicados.add(elemento)
print("Conjunto sem elementos duplicados:", sem_duplicados)