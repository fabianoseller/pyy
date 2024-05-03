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


class ProdutoEletronico:
    def __init__(self, codigo, nome, marca, modelo, preco, tipo):
        self.codigo = codigo
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.tipo = tipo
    
    def aplicar_garantia_estendida(self, preco_garantia):
        self.preco += preco_garantia
    
    def calcular_valor_total(self):
        return self.preco
    
    def mostrar_informacoes(self):
        print("Código:", self.codigo)
        print("Nome:", self.nome)
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Preço:", self.preco)
        print("Tipo:", self.tipo)


class Restaurante:
    def __init__(self, nome, especialidade, endereco, horario_funcionamento):
        self.nome = nome
        self.especialidade = especialidade
        self.endereco = endereco
        self.horario_funcionamento = horario_funcionamento
        self.cardapio = []
    
    def adicionar_prato(self, nome_prato, descricao, preco):
        self.cardapio.append({"Nome": nome_prato, "Descrição": descricao, "Preço": preco})
    
    def remover_prato(self, nome_prato):
        for prato in self.cardapio:
            if prato["Nome"] == nome_prato:
                self.cardapio.remove(prato)
                break
    
    def mostrar_cardapio(self):
        print("Cardápio de", self.nome)
        for prato in self.cardapio:
            print("Nome:", prato["Nome"])
            print("Descrição:", prato["Descrição"])
            print("Preço:", prato["Preço"])
            print()  # Adiciona uma linha em branco entre os pratos
            

class AgendaTelefonica:
    def __init__(self):
        self.contatos = []
    
    def adicionar_contato(self, nome, telefone, email):
        self.contatos.append({"Nome": nome, "Telefone": telefone, "Email": email})
    
    def buscar_contato(self, chave):
        for contato in self.contatos:
            if chave in contato.values():
                return contato
        return None
    
    def remover_contato(self, chave):
        contato = self.buscar_contato(chave)
        if contato:
            self.contatos.remove(contato)
    
    def mostrar_contatos(self):
        print("Lista de Contatos:")
        for contato in self.contatos:
            print("Nome:", contato["Nome"])
            print("Telefone:", contato["Telefone"])
            print("Email:", contato["Email"])
            print()


class JogoEletronico:
    def __init__(self, nome, genero, plataforma, classificacao_indicativa, preco):
        self.nome = nome
        self.genero = genero
        self.plataforma = plataforma
        self.classificacao_indicativa = classificacao_indicativa
        self.preco = preco
    
    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * percentual / 100
    
    def calcular_valor_total(self):
        return self.preco
    
    def mostrar_informacoes(self):
        print("Nome:", self.nome)
        print("Gênero:", self.genero)
        print("Plataforma:", self.plataforma)
        print("Classificação Indicativa:", self.classificacao_indicativa)
        print("Preço:", self.preco)
