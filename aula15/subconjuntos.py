#Crie um conjunto com os países da América do Sul e outro com os países que você já visitou.
#Verifique se o conjunto dos países que você já visitou é um subconjunto do conjunto dos países da América do Sul.


# Subconjuntos
paises_america_sul = {"Brasil", "Argentina", "Chile", "Colômbia", "Peru"}
paises_visitados = {"Brasil", "Argentina", "Uruguai"}
if paises_visitados.issubset(paises_america_sul):
    print("Você já visitou todos os países da América do Sul.")
else:
    print("Você não visitou todos os países da América do Sul.")