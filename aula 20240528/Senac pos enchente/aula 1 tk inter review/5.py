import tkinter as tk

def mostrar_selecao():
  selecao = var_selecao.get()
  rotulo_selecao.config(text=f"Você selecionou: {selecao}")

janela = tk.Tk()
janela.title("Exemplo de Radio Buttons")

rotulo_selecao = tk.Label(janela, text="")
rotulo_selecao.pack(pady=20)

var_selecao = tk.StringVar(value="opcao1")  # Define "Opção 1" como selecionada inicialmente

radio_opcao1 = tk.Radiobutton(janela, text="Opção 1", variable=var_selecao, value="opcao1", command=mostrar_selecao)
radio_opcao1.pack(pady=5)

radio_opcao2 = tk.Radiobutton(janela, text="Opção 2", variable=var_selecao, value="opcao2", command=mostrar_selecao)
radio_opcao2.pack(pady=5)

radio_opcao3 = tk.Radiobutton(janela, text="Opção 3", variable=var_selecao, value="opcao3", command=mostrar_selecao)
radio_opcao3.pack(pady=5)

janela.mainloop()