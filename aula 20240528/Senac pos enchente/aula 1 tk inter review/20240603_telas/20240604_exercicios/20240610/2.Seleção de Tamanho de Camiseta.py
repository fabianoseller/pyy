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

botao_sair = tk.Button(root, text="Sair", command=root.quit)
botao_sair.pack()

root.mainloop() 

# xx Importação de Bibliotecas O código começa com a importação de duas bibliotecas:
# import tkinter as tk: Importa a biblioteca Tkinter, que é usada para criar janelas gráficas em Python.


# Definição da Função escolher_tamanho
# A função escolher_tamanho é definida para ser executada quando o botão "Escolher" é clicado. Essa função:
# Obtém o valor escolhido no menu de opções opcao_tamanho usando o método get().
# Cria uma mensagem com o texto "Você escolheu o tamanho: {tamanho}", onde {tamanho} é substituído pelo valor escolhido.
# Atualiza o texto do rótulo label_resultado com a mensagem criada.
#  Criação da Janela
#  A janela principal é criada com o comando root = tk.Tk(), que cria uma janela com o título "Seleção de Tamanho de Camiseta".
#  Componentes da Janela
# Os componentes da janela são criados usando os widgets Tkinter:
#  label_tamanho: Um rótulo que exibe a mensagem "Escolha o tamanho da sua camiseta:".
# opcoes_tamanho: Uma lista de opções que contém os tamanhos de camiseta ("P", "M", "G", "GG").
# opcao_tamanho: Uma variável de string que armazena o valor escolhido no menu de opções.
# menu_tamanho: Um menu de opções que exibe as opções de tamanho de camiseta.
# botao_escolher: Um botão que executa a função escolher_tamanho quando clicado.
# label_resultado: Um rótulo que exibe o resultado da escolha do tamanho de camiseta.

