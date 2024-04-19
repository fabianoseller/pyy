
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


ponto = PontoGeografico(40.7128, -74.0060)
print("Latitude do ponto:", ponto.get_latitude())

ponto.set_latitude(37.7749)

print("Longitude do ponto:", ponto.get_longitude())
ponto.set_longitude(-122.4194)
