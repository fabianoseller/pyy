import random #import random: Importa o módulo random para embaralhar as cartas.
class Carta:
    def __init__(self, valor, naipe):#Construtor da classe Carta.
        self.valor = valor
        self.naipe = naipe
     #Define os atributos valor (valor da carta) e naipe (naipe da carta).

    def __str__(self):
        return f"{self.valor} de {self.naipe}"#Define a representação em string da carta. Retorna uma string no formato "{valor} de {naipe}".

class CartaBaralho(Carta):
    def __init__(self, valor, naipe):#Chama o construtor da classe base (Carta) com os mesmos argumentos.
        super().__init__(valor, naipe)

    def comparar(self, outra_carta):#Compara a carta atual com outra_carta.Retorna:1 se a carta atual for maior que outra_carta.-1 se a carta atual for menor que outra_carta.0 se as cartas forem iguais em valor e naipe.
        if self.valor > outra_carta.valor:
            return 1
        elif self.valor < outra_carta.valor:
            return -1
        else:
            if self.naipe > outra_carta.naipe:
                return 1
            elif self.naipe < outra_carta.naipe:
                return -1
            else:
                return 0

class Baralho:
    def __init__(self):#Construtor da classe Baralho.Cria um baralho padrão com 52 cartas:13 cartas de cada naipe ("Espadas", "Ouros", "Copas", "Paus").Valores de 1 a 13 para cada naipe.
        self.cartas = []
        for naipe in ["Espadas", "Ouros", "Copas", "Paus"]:
            for valor in range(1, 14):
                self.cartas.append(CartaBaralho(valor, naipe))

    def embaralhar(self):#Embaralha as cartas do baralho usando a função shuffle do módulo random.
        random.shuffle(self.cartas)#A função shuffle recebe como argumento uma lista como entrada e modifica-a diretamente no lugar, embaralhando a ordem dos seus elementos.

    def distribuir(self, jogadores, num_cartas_por_jogador):
        for jogador in jogadores:
            jogador.cartas = self.cartas[:num_cartas_por_jogador]
            del self.cartas[:num_cartas_por_jogador]
# Distribui as cartas do baralho para os jogadores.
# Argumentos:
# jogadores: Lista de objetos Jogador.
# num_cartas_por_jogador: Número de cartas a serem distribuídas para cada jogador.
# Funciona da seguinte maneira:
# Para cada jogador:
# Atribui as num_cartas_por_jogador primeiras cartas do baralho para o jogador.
# Remove essas cartas do baralho.

    def mostrar_cartas(self):
        for carta in self.cartas:
            print(carta)
# mostrar_cartas(self):
# Mostra todas as cartas do baralho.
# Usa um loop for para imprimir cada carta usando a representação em string (__str__).
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []
# __init__(self, nome):
# Construtor da classe Jogador.
# Define o atributo nome do jogador.
# Inicializa a lista cartas como vazia.

    def mostrar_cartas(self):
        print(f"Cartas de {self.nome}:")
        for carta in self.cartas:
            print(carta)
# mostrar_cartas(self):
# Mostra todas as cartas do jogador.
# Usa um loop for para imprimir cada carta usando a representação em string (__str__).

# Criação do baralho
baralho = Baralho()#Cria um novo objeto Baralho.

# Embaralhar o baralho
baralho.embaralhar()#Embaralha as cartas do baralho.

# Criando jogadores
jogadores = [Jogador("João"), Jogador("Maria")]#Cria uma lista de dois jogadores, "João" e "Maria".

# Distribuindo cartas
baralho.distribuir(jogadores, 2)# Distribui 2 cartas para cada jogador.

# Mostrando cartas dos jogadores
for jogador in jogadores:#Um loop for para iterar sobre cada jogador na lista.
    jogador.mostrar_cartas()#Chama o método mostrar_cartas do jogador para mostrar suas cartas.

# Comparação de cartas (opcional)
carta_jogador_1 = jogadores[0].cartas[0]# Obtém a primeira carta do primeiro jogador.
carta_jogador_2 = jogadores[1].cartas[0]# Obtém a primeira carta do segundo jogador.

resultado_comparacao = carta_jogador_1.comparar(carta_jogador_2)#Compara as duas cartas usando o método comparar da classe CartaBaralho.

if resultado_comparacao > 0:# Se a primeira carta for maior, exibe uma mensagem informando o vencedor.
    print(f"A carta de {jogadores[0].nome} ({carta_jogador_1}) vence a carta de {jogadores[1].nome} ({carta_jogador_2})")
elif resultado_comparacao < 0:#Se a segunda carta for maior, exibe uma mensagem informando o vencedor.
    print(f"A carta de {jogadores[1].nome} ({carta_jogador_2}) vence a carta de {jogadores[0].nome} ({carta_jogador_1})")
else:
    print("As cartas são iguais!")