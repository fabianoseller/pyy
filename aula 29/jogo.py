
class Jogo(ABC):
    def __init__(self, nome, genero, plataforma, classificacao_indicativa):
        self.nome = nome
        self.genero = genero
        self.plataforma = plataforma
        self.classificacao_indicativa = classificacao_indicativa
    
    @abstractmethod
    def iniciar(self):
        pass
    
    @abstractmethod
    def pausar(self):
        pass
    
    @abstractmethod
    def salvar_jogo(self):
        pass
    
    @abstractmethod
    def carregar_jogo(self):
        pass

class RPG(Jogo):
    def iniciar(self):
        print("Iniciando jogo de RPG.")
    
    def pausar(self):
        print("Jogo de RPG pausado.")
    
    def salvar_jogo(self):
        print("Salvando progresso do jogo de RPG.")
    
    def carregar_jogo(self):
        print("Carregando jogo de RPG.")

class Aventura(Jogo):
    def iniciar(self):
        print("Iniciando jogo de aventura.")
    
    def pausar(self):
        print("Jogo de aventura pausado.")
    
    def salvar_jogo(self):
        print("Salvando progresso do jogo de aventura.")
    
    def carregar_jogo(self):
        print("Carregando jogo de aventura.")

class Estrategia(Jogo):
    def iniciar(self):
        print("Iniciando jogo de estratégia.")
    
    def pausar(self):
        print("Jogo de estratégia pausado.")
    
    def salvar_jogo(self):
        print("Salvando progresso do jogo de estratégia.")
    
    def carregar_jogo(self):
        print("Carregando jogo de estratégia.")
