import tkinter as tk

def mostrar_nome():
    texto = entrada.get()
    rotulo_nome.config(text=texto)

janela = tk.Tk()
janela.title("Manipulando Texto")

entrada = tk.Entry(janela)
entrada.pack()

botao_mostrar = tk.Button(janela, text="Mostrar Nome", command=mostrar_nome)
botao_mostrar.pack()

rotulo_nome = tk.Label(janela, text="")
rotulo_nome.pack()

janela.mainloop()