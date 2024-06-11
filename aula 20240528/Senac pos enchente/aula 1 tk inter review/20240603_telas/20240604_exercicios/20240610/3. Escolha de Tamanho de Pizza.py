import tkinter as tk
from tkinter import ttk

# Fluxo de Execução
# O usuário escolhe o tamanho da pizza no menu de opções.
# O usuário digita a quantidade de pizzas no campo de entrada.
# O usuário clica no botão "Pedir".
# A função pedir_pizza é executada, calculando o total a pagar com base no tamanho e quantidade de pizzas escolhidas.
# O resultado é exibido no rótulo label_resultado.

# Observações
# O código utiliza a biblioteca tkinter para criar a janela e componentes gráficos.
# A função pedir_pizza utiliza a variável opcao_tamanho para obter a opção escolhida pelo usuário e calcular o total a pagar.
# O código utiliza a função pack para organizar os componentes na janela.
# O código utiliza a função mainloop para iniciar o loop principal da janela, permitindo que o aplicativo interaja com o usuário.

def pedir_pizza():
    tamanho = opcao_tamanho.get()
    quantidade = int(entrada_quantidade.get())
    if tamanho == "Pequena":
        preco = 10
    elif tamanho == "Média":
        preco = 15
    elif tamanho == "Grande":
        preco = 20
    total = preco * quantidade
    mensagem = f"O total a pagar é: R$ {total:.2f}"
    label_resultado.config(text=mensagem)

root = tk.Tk()
root.title("Pedir Pizza")

## Escolha de Tamanho
label_tamanho = tk.Label(root, text="Escolha o tamanho da pizza:")
label_tamanho.pack()

opcoes_tamanho = ["Pequena", "Média", "Grande"]
opcao_tamanho = tk.StringVar()
opcao_tamanho.set(opcoes_tamanho[0])

menu_tamanho = tk.OptionMenu(root, opcao_tamanho, *opcoes_tamanho)
menu_tamanho.pack()

## Quantidade de Pizzas
label_quantidade = tk.Label(root, text="Quantidade de pizzas:")
label_quantidade.pack()

entrada_quantidade = tk.Entry(root)
entrada_quantidade.pack()

## Botão para pedir
botao_pedir = tk.Button(root, text="Pedir", command=pedir_pizza)
botao_pedir.pack()

## Exibir resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack()

botao_sair = tk.Button(root, text="Sair", command=root.quit)
botao_sair.pack()

root.mainloop()
# teste 



