class PontoGeografico:
  def __init__(self, latitude, longitude):
    self.latitude = latitude
    self.longitude = longitude

  # Getter para latitude
  def get_latitude(self):
    return self.latitude

  # Setter para latitude
  def set_latitude(self, nova_latitude):
    if -90 <= nova_latitude <= 90:
      self.latitude = nova_latitude
    else:
      print("Latitude inválida. Deve estar entre -90 e 90 graus.")

  # Getter para longitude
  def get_longitude(self):
    return self.longitude

  # Setter para longitude
  def set_longitude(self, nova_longitude):
    if -180 <= nova_longitude <= 180:
      self.longitude = nova_longitude
    else:
      print("Longitude inválida. Deve estar entre -180 e 180 graus.")

# Criando um objeto da classe PontoGeografico
ponto = PontoGeografico(-29.971047, -54.333333)  # Latitude e longitude de Porto Alegre, RS

# Acessando e imprimindo a latitude do ponto
print(f"Latitude: {ponto.get_latitude():.6f}")

# Alterando a latitude do ponto
ponto.set_latitude(-30.051047)  # Latitude de Gramado, RS

# Acessando e imprimindo a nova latitude do ponto
print(f"Nova latitude: {ponto.get_latitude():.6f}")

# Acessando e imprimindo a longitude do ponto
print(f"Longitude: {ponto.get_longitude():.6f}")

# Alterando a longitude do ponto
ponto.set_longitude(-54.616667)  # Longitude de Gramado, RS

# Acessando e imprimindo a nova longitude do ponto
print(f"Nova longitude: {ponto.get_longitude():.6f}")