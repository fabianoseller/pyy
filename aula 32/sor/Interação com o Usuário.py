import tkinter as tk

def mudar_cor():
    cor_atual = rotulo.cget("bg")
    nova_cor = "green" if cor_atual == "red" else "red"
    rotulo.config(bg=nova_cor)

janela = tk.Tk()
janela.title("Interação com o Usuário")

rotulo = tk.Label(janela, text="Clique para Mudar Cor", bg="red")
rotulo.pack()

botao_cor = tk.Button(janela, text="Clique para Mudar Cor", command=mudar_cor)
botao_cor.pack()

janela.mainloop()