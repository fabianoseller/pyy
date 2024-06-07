import tkinter as tk
import os

def carregar_texto():
    try:
        arquivo_nome = caixa_entrada_nome_arquivo.get()
        if not arquivo_nome:
            raise Exception("Nome do arquivo inválido")

        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        arquivo_completo = os.path.join(diretorio_script, arquivo_nome)

        if not os.path.exists(arquivo_completo):
            raise Exception("Arquivo não encontrado")

        if os.path.isdir(arquivo_completo):
            raise Exception("Caminho especificado é um diretório")

        with open(arquivo_completo, "r") as arquivo:
            texto.delete(1.0, tk.END)
            texto.insert(tk.END, arquivo.read())
            mensagem_status.config(text=f"Texto carregado com sucesso. Quantidade de letras: {len(texto.get(1.0, tk.END))}")

    except Exception as e:
        mensagem_status.config(text=f"Erro ao carregar: {e}")

def salvar_texto():
    try:
        arquivo_nome = caixa_entrada_nome_arquivo.get()
        if not arquivo_nome:
            raise Exception("Nome do arquivo inválido")

        diretorio_script = os.path.dirname(os.path.abspath(__file__))
        arquivo_completo = os.path.join(diretorio_script, arquivo_nome)

        if os.path.exists(arquivo_completo):
            raise Exception("Arquivo já existe")

        with open(arquivo_completo, "w") as arquivo:
            arquivo.write(texto.get(1.0, tk.END))
            mensagem_status.config(text=f"Texto salvo com sucesso em '{arquivo_completo}'. Quantidade de letras: {len(texto.get(1.0, tk.END))}")

    except Exception as e:
        mensagem_status.config(text=f"Erro ao salvar: {e}")

# Criar a janela principal
janela = tk.Tk()
janela.title("Carregar Texto de Arquivo")

# Criar o widget Text
texto = tk.Text(janela, width=60, height=20)
texto.pack(padx=10, pady=10)

# Criar área de entrada para nome do arquivo
caixa_entrada_nome_arquivo = tk.Entry(janela)
caixa_entrada_nome_arquivo.pack(pady=5)

# Criar botão para carregar texto
botao_carregar_texto = tk.Button(janela, text="Carregar Texto", command=carregar_texto)
botao_carregar_texto.pack(pady=5)

# Criar botão para salvar texto
botao_salvar_texto = tk.Button(janela, text="Salvar Texto", command=salvar_texto)
botao_salvar_texto.pack(pady=5)

# Criar área de texto para exibir a mensagem de status
mensagem_status = tk.Label(janela, text="")
mensagem_status.pack(pady=5)

# Executar o loop principal da interface
janela.mainloop()
