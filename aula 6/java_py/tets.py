import json
import datetime
import os

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.isoformat()
        return super().default(o)

class Usuario:
    def __init__(self, nome, email, cidade):
        self.nome = nome
        self.email = email
        self.cidade = cidade

class Evento:
    def __init__(self, nome, endereco, categoria, horario, descricao):
        self.nome = nome
        self.endereco = endereco
        self.categoria = categoria
        self.horario = horario
        self.descricao = descricao

class Sistema:
    def __init__(self):
        self.usuarios = []
        self.eventos = []
        self.carregar_eventos()

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def cadastrar_evento(self, evento):
        self.eventos.append(evento)

    def carregar_eventos(self):
        if os.path.exists("dados.json") and os.path.getsize("dados.json") > 0:
            try:
                with open("dados.json", "r") as file:
                    data = json.load(file)
                    for evento_data in data["eventos"]:
                        horario = datetime.datetime.fromisoformat(evento_data["horario"])
                        evento = Evento(evento_data["nome"], evento_data["endereco"], evento_data["categoria"], horario, evento_data["descricao"])
                        self.eventos.append(evento)
            except (json.JSONDecodeError, KeyError):
                print("O arquivo de dados está corrompido ou em um formato inválido.")
        else:
            print("O arquivo de dados está vazio ou não existe.")

    def salvar_eventos(self):
        with open("dados.json", "w") as file:
            data = {
                "eventos": [evento.__dict__ for evento in self.eventos]
            }
            json.dump(data, file, cls=DateTimeEncoder, indent=4)

    def consultar_eventos(self):
        print("Eventos disponíveis:")
        for evento in sorted(self.eventos, key=lambda x: x.horario):
            print(f"{evento.nome} - {evento.horario}")

    def participar_evento(self, usuario, evento):
        print(f"{usuario.nome} está participando do evento: {evento.nome}")
        # Aqui você pode implementar a lógica para adicionar o usuário à lista de participantes do evento

    def cancelar_participacao(self, usuario, evento):
        print(f"{usuario.nome} cancelou sua participação no evento: {evento.nome}")
        # Aqui você pode implementar a lógica para remover o usuário da lista de participantes do evento

    def notificar_eventos(self):
        now = datetime.datetime.now()
        eventos_proximos = [evento for evento in self.eventos if evento.horario > now]
        if eventos_proximos:
            print("Eventos próximos:")
            for evento in eventos_proximos:
                print(f"{evento.nome} - {evento.horario}")
        else:
            print("Não há eventos próximos.")

# Instanciando o sistema
sistema = Sistema()

# Cadastrando eventos
evento1 = Evento("Festa de Aniversário", "Rua A, 123", "Festa", datetime.datetime(2024, 3, 2, 20, 0), "Venha comemorar meu aniversário!")
evento2 = Evento("Corrida Beneficente", "Parque B", "Eventos Esportivos", datetime.datetime(2024, 3, 5, 9, 0), "Corrida para arrecadar fundos para a caridade")
sistema.cadastrar_evento(evento1)
sistema.cadastrar_evento(evento2)

# Consultar eventos
sistema.consultar_eventos()

# Salvar eventos no arquivo JSON
sistema.salvar_eventos()

# Notificar eventos próximos
sistema.notificar_eventos()
