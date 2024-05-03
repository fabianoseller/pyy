import tkinter as tk

# Criar a janela principal
janela = tk.Tk()
janela.title("Minha Janela")
janela.geometry("300x200+100+100")

# Adicionar um rótulo e um botão
rotulo = tk.Label(janela, text="Olá, Mundo!")
rotulo.pack()

botao = tk.Button(janela, text="Clique em Mim")
botao.pack()

janela.mainloop()