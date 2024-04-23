saldo = 0

while True:
  operacao = input("Digite a operação desejada (saldo, saque, deposito, sair): ")

  if operacao == "saldo":
    print(f"Saldo: R${saldo}")
  elif operacao == "saque":
    valor_saque = float(input("Digite o valor do saque: "))

    if valor_saque <= saldo:
      saldo -= valor_saque
      print(f"Saque realizado com sucesso. Saldo atual: R${saldo}")
    else:
      print("Saldo insuficiente.")
  elif operacao == "deposito":
    valor_deposito = float(input("Digite o valor do depósito: "))
    saldo += valor_deposito
    print(f"Depósito realizado com sucesso. Saldo atual: R${saldo}")
  elif operacao == "sair":
    break
  else:
    print("Operação inválida.")

