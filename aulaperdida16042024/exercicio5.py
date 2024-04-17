#a classe PontoGeografico com os atributos latitude e 
# longitude, e implementamos os métodos getters e setters
# para cada um deles. Em seguida, criamos uma 
# instância dessa classe (ponto) e realizamos as operações
# solicitadas: acessar/imprimir e alterar a latitude e a longitude do ponto geográfico.

class PontoGeografico:
    def __init__(self, latitude, longitude):
        self.__latitude = latitude
        self.__longitude = longitude

    # Getters
    def get_latitude(self):
        return self.__latitude

    def get_longitude(self):
        return self.__longitude

    # Setters
    def set_latitude(self, nova_latitude):
        self.__latitude = nova_latitude
        print("Latitude do ponto alterada para:", nova_latitude)

    def set_longitude(self, nova_longitude):
        self.__longitude = nova_longitude
        print("Longitude do ponto alterada para:", nova_longitude)

# Criando um objeto da classe PontoGeografico
ponto = PontoGeografico(40.7128, -74.0060)

# Acessando e imprimindo a latitude do ponto
print("Latitude do ponto:", ponto.get_latitude())

# Alterando a latitude do ponto
ponto.set_latitude(37.7749)

# Acessando e imprimindo a longitude do ponto
print("Longitude do ponto:", ponto.get_longitude())

# Alterando a longitude do ponto
ponto.set_longitude(-122.4194)
