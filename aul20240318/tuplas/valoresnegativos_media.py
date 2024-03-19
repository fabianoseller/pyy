lista = [(3, 8, -1, 2), (2, -2, 4, 2), (7, 5, 3, -9)]
medias_negativas = []

# Calculando a média dos valores negativos em cada tupla
for tupla in lista:
    valores_negativos = [valor for valor in tupla if valor < 0]
    if valores_negativos:  # Verifica se há valores negativos na tupla
        media_negativos = sum(valores_negativos) / len(valores_negativos)
        medias_negativas.append(media_negativos)

print("As médias dos valores negativos em cada tupla são:")
for i, media in enumerate(medias_negativas, 1):
    print(f"Tupla {i}: {media}")
