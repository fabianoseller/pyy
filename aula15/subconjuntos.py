#Crie um conjunto com os países da América do Sul e outro com os países que você já visitou.
#Verifique se o conjunto dos países que você já visitou é um subconjunto do conjunto dos países da América do Sul.

<<<<<<< HEAD
paises_america_sul = {'Brasil', 'Argentina', 'Chile', 'Colômbia', 'Peru'}
paises_visitados = {'Brasil', 'Argentina', 'Chile'}

if paises_visitados.issubset(paises_america_sul):
    print("Você visitou todos os países da América do Sul!")
else:
    print("Há países na América do Sul que você ainda não visitou.")
=======

# Subconjuntos
paises_america_sul = {"Brasil", "Argentina", "Chile", "Colômbia", "Peru"}
paises_visitados = {"Brasil", "Argentina", "Uruguai"}
if paises_visitados.issubset(paises_america_sul):
    print("Você já visitou todos os países da América do Sul.")
else:
    print("Você não visitou todos os países da América do Sul.")
>>>>>>> cfdb00bf729536818231734432b7b3f9555cb6c1
