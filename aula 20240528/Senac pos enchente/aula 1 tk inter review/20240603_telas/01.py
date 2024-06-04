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
def carregar_texto():
    try:
        arquivo_nome = caixa_entrada_nome_arquivo.get()
        if not arquivo_nome:
            raise Exception("Nome do arquivo inválido")

        if not os.path.exists(arquivo_nome):
            raise Exception("Arquivo não encontrado")

        if os.path.isdir(arquivo_nome):
            raise Exception("Caminho especificado é um diretório")

        with open(arquivo_nome, "r") as arquivo:
            texto.delete(1.0, tk.END)
            texto.insert(tk.END, arquivo.read())
        mensagem_status.config(text=f"Texto carregado de '{arquivo_nome}'")
    except Exception as e:
        mensagem_status.config(text=f"Erro ao carregar: {e}")
def limpar_texto():
    texto.delete(1.0, tk.END)
# Criar a janela principal
janela = tk.Tk()
janela.title("Criador de Arquivos TXT")

# Criar o widget Text
texto = tk.Text(janela, width=60, height=20)
texto.pack(padx=10, pady=10)

# Criar área de entrada para nome do arquivo
caixa_entrada_nome_arquivo = tk.Entry(janela)
caixa_entrada_nome_arquivo.pack(pady=5)

# Criar botão para salvar texto
botao_salvar_texto = tk.Button(janela, text="Salvar Texto", command=salvar_texto)
botao_salvar_texto.pack(pady=5)

# Criar botão para carregar texto
botao_carregar_texto = tk.Button(janela, text="Carregar Texto", command=carregar_texto)
botao_carregar_texto.pack(pady=5)

# Criar área de texto para exibir a mensagem de status
mensagem_status = tk.Label(janela, text="")
mensagem_status.pack(pady=5)

botao_limpar_texto = tk.Button(janela, text="Limpar Texto", command=limpar_texto)
botao_limpar_texto.pack(pady=5)
# Executar o loop principal da interface
janela.mainloop()