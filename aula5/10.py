estoque = 1000

while True:
    operacao = input("Digite a operação desejada (estoque, entrada, saida, sair): ")

    if operacao == "saldo":
        print(f"Saldo: {estoque}")
    elif operacao == "entrada":
        valor_entrada = float(input("Digite o valor da entrada: "))
        estoque += valor_entrada
        print(f"Entrada realizada com sucesso. Saldo atual: {estoque}")
    elif operacao == "saida":
        valor_saida = float(input("Digite o valor da saida: "))
        if valor_saida <= estoque:
            estoque -= valor_saida
            print(f"Saída realizada com sucesso. Saldo atual: {estoque}")
        else:
            print("Saldo insuficiente.")
    elif operacao == "sair":
        break
    else:
        print("Operação inválida.")