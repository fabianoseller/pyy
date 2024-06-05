import tkinter as tk
import os

def salvar_texto():
    try:
        arquivo_nome = caixa_entrada_nome_arquivo.get()
        if not arquivo_nome:
            raise Exception("Nome do arquivo inválido")

        with open(arquivo_nome, "w") as arquivo:
            arquivo.write(texto.get(1.0, tk.END))
        mensagem_status.config(text=f"Texto salvo em '{arquivo_nome}'")
    except Exception as e:
        mensagem_status.config(text=f"Erro ao salvar: {e}")


# Criar a janela principal
janela = tk.Tk()
janela.title("Salvar Texto em Arquivo")

# Criar o widget Text
texto = tk.Text(janela, width=60, height=20)
texto.pack(padx=10, pady=10)

# Criar área de entrada para nome do arquivo
caixa_entrada_nome_arquivo = tk.Entry(janela)
caixa_entrada_nome_arquivo.pack(pady=5)

# Criar botão para salvar texto
botao_salvar_texto = tk.Button(janela, text="Salvar Texto", command=salvar_texto)
botao_salvar_texto.pack(pady=5)



# Criar área de texto para exibir a mensagem de status
mensagem_status = tk.Label(janela, text="")
mensagem_status.pack(pady=5)

# Executar o loop principal da interface
janela.mainloop()