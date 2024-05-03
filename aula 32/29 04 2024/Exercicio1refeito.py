import tkinter as tk
from tkinter import ttk

def fechar_janela():
    root.destroy()

def limpar_texto():
    entrada_texto.delete(0, 'end')

def atualizar_rotulo():
    opcao_selecionada = ""
    if var_opcao1.get():
        opcao_selecionada += "Opção 1 "
    if var_opcao2.get():
        opcao_selecionada += "Opção 2 "
    if var_opcao3.get():
        opcao_selecionada += "Opção 3 "
        
    rotulo_selecionado.config(text="Selecionado: " + opcao_selecionada)

def atualizar_menu(event):
    opcao_selecionada = menu_var.get()
    rotulo_menu.config(text="Selecionado: " + opcao_selecionada)

root = tk.Tk()
root.title("Minha Primeira Interface")

# Rótulo inicial
rotulo_inicial = tk.Label(root, text="Olá, Tkinter!")
rotulo_inicial.pack()

# Botão para fechar a janela
botao_fechar = tk.Button(root, text="Clique em Mim", command=fechar_janela)
botao_fechar.pack()

# Campo de entrada de texto
entrada_texto = tk.Entry(root)
entrada_texto.pack()

# Botão para limpar o texto
botao_limpar = tk.Button(root, text="Limpar", command=limpar_texto)
botao_limpar.pack()

# Caixas de seleção
var_opcao1 = tk.BooleanVar()
var_opcao2 = tk.BooleanVar()
var_opcao3 = tk.BooleanVar()

check_opcao1 = tk.Checkbutton(root, text="Opção 1", variable=var_opcao1, command=atualizar_rotulo)
check_opcao1.pack()

check_opcao2 = tk.Checkbutton(root, text="Opção 2", variable=var_opcao2, command=atualizar_rotulo)
check_opcao2.pack()

check_opcao3 = tk.Checkbutton(root, text="Opção 3", variable=var_opcao3, command=atualizar_rotulo)
check_opcao3.pack()

# Rótulo para exibir seleções das caixas de seleção
rotulo_selecionado = tk.Label(root, text="Selecionado: ")
rotulo_selecionado.pack()

# Menu suspenso
opcoes_menu = ["Opção A", "Opção B", "Opção C", "Opção D"]
menu_var = tk.StringVar(root)
menu_var.set(opcoes_menu[0])

menu = ttk.Combobox(root, textvariable=menu_var, values=opcoes_menu)
menu.pack()
menu.bind("<<ComboboxSelected>>", atualizar_menu)

# Rótulo para exibir opção selecionada no menu
rotulo_menu = tk.Label(root, text="Selecionado a partir do label: ")
rotulo_menu.pack()

root.mainloop()
