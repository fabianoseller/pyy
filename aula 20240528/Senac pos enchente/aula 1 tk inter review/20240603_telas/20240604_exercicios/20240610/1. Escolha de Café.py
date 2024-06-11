import tkinter as tk
from tkinter import ttk

def escolher_cafe():
    escolha = opcao_cafe.get()
    mensagem = f"Você escolheu: {escolha}"
    label_resultado.config(text=mensagem)

root = tk.Tk()
root.title("Menu de Café")

## Escolha de Café
label_cafe = tk.Label(root, text="Escolha seu café preferido:")
label_cafe.pack()

opcoes_cafe = ["Expresso", "Cappuccino", "Latte Macchiato"]
opcao_cafe = tk.StringVar()
opcao_cafe.set(opcoes_cafe[0])

menu_cafe = tk.OptionMenu(root, opcao_cafe, *opcoes_cafe)
menu_cafe.pack()

## Botão para escolher
botao_escolher = tk.Button(root, text="Escolher", command=escolher_cafe)
botao_escolher.pack()

## Exibir resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack()

root.mainloop() 
