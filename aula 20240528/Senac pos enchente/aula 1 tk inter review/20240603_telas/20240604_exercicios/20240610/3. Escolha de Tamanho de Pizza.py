import tkinter as tk
from tkinter import ttk

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

root.mainloop()
# teste 

