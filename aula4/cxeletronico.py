
class CaixaEletronico:

   def __init__(self):
       self.saldo = 0
       self.movimentacoes = []
   def deposito(self, valor):
       self.saldo += valor
       self.movimentacoes.append(f'Depósito de R$ {valor:.2f}')

   def saque(self, valor):

       if valor > self.saldo:

           print('Saldo insuficiente')

       else:

           self.saldo -= valor

           self.movimentacoes.append(f'Saque de R$ {valor:.2f}')

   def pagamento_de_conta(self, valor, descricao):

       if valor > self.saldo:

           print('Saldo insuficiente')

       else:

           self.saldo -= valor

           self.movimentacoes.append(f'Pagamento de conta: {descricao} no valor de R$ {valor:.2f}')

   def extrato(self):

       print(f'Saldo: R$ {self.saldo:.2f}')

       for movimentacao in self.movimentacoes:

           print(movimentacao)