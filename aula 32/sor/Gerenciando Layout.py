import tkinter as tk

janela = tk.Tk()
janela.title("Gerenciando Layout")

frame = tk.Frame(janela)
frame.pack()

botao1 = tk.Button(frame, text="Botão 1")
botao1.pack(side=tk.LEFT)

botao2 = tk.Button(frame, text="Botão 2")
botao2.pack(side=tk.LEFT)

botao3 = tk.Button(frame, text="Botão 3")
botao3.pack(side=tk.LEFT)

janela.mainloop()