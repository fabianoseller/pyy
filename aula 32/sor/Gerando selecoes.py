import tkinter as tk

def mostrar_selecao():
    selecao = listbox.curselection()
    if selecao:
        indice = selecao[0]
        valor = listbox.get(indice)
        rotulo_selecao.config(text=valor)

janela = tk.Tk()
janela.title("Gerenciando Seleções")

listbox = tk.Listbox(janela)
listbox.pack()

opcoes = ["Opção 1", "Opção 2", "Opção 3"]
for opcao in opcoes:
    listbox.insert(tk.END, opcao)

botao_mostrar_selecao = tk.Button(janela, text="Mostrar Seleção", command=mostrar_selecao)
botao_mostrar_selecao.pack()

rotulo_selecao = tk.Label(janela, text="")
rotulo_selecao.pack()

janela.mainloop()