class Voo:
    def __init__(self, codigo, companhia, origem, destino, horario_saida, horario_chegada, preco_passagem):
        self.codigo = codigo
        self.companhia = companhia
        self.origem = origem
        self.destino = destino
        self.horario_saida = horario_saida
        self.horario_chegada = horario_chegada
        self.preco_passagem = preco_passagem
    
    def calcular_duracao_voo(self):
        return self.horario_chegada - self.horario_saida
    
    def aplicar_desconto(self, percentual):
        self.preco_passagem -= self.preco_passagem * percentual / 100
    
    def mostrar_informacoes(self):
        print("Código:", self.codigo)
        print("Companhia:", self.companhia)
        print("Origem:", self.origem)
        print("Destino:", self.destino)
        print("Horário de Saída:", self.horario_saida)
        print("Horário de Chegada:", self.horario_chegada)
        print("Preço da Passagem com Desconto:", self.preco_passagem)

