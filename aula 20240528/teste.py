import tkinter as tk

janela = tk.Tk()
janela.title("Minha Aplicação")
janela.geometry("300x200")

rotulo = tk.Label(janela, text="Olá, Mundo!")
rotulo.pack()

botao = tk.Button(janela, text="Clique aqui")
botao.pack()

janela.mainloop()
