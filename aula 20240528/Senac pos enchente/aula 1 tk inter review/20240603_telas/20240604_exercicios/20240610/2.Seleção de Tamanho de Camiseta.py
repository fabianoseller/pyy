import tkinter as tk
from tkinter import ttk

def escolher_tamanho():
    tamanho = opcao_tamanho.get()
    mensagem = f"Você escolheu o tamanho: {tamanho}"
    label_resultado.config(text=mensagem)

root = tk.Tk()
root.title("Seleção de Tamanho de Camiseta")

## Escolha de Tamanho
label_tamanho = tk.Label(root, text="Escolha o tamanho da sua camiseta:")
label_tamanho.pack()

opcoes_tamanho = ["P", "M", "G", "GG"]
opcao_tamanho = tk.StringVar()
opcao_tamanho.set(opcoes_tamanho[0])

menu_tamanho = tk.OptionMenu(root, opcao_tamanho, *opcoes_tamanho)
menu_tamanho.pack()

## Botão para escolher
botao_escolher = tk.Button(root, text="Escolher", command=escolher_tamanho)
botao_escolher.pack()

## Exibir resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack()

root.mainloop() 

# xx

