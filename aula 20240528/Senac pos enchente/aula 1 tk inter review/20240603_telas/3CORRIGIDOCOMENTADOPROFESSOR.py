# 3 Salvar Texto em Arquivo:
# Crie uma função que permita ao usuário salvar o conteúdo do campo Text em um arquivo de texto.
# Exiba uma mensagem de sucesso ou erro após a operação.

import tkinter as tk

import os

def salvar_texto():
  try:
    # Obter o nome do arquivo do campo de entrada
    arquivo_nome = caixa_entrada_nome_arquivo.get()

    # Validar o nome do arquivo
    if not arquivo_nome:
      raise Exception("Nome do arquivo inválido")

    # Separar nome e extensão (se houver)
    nome, extensao = os.path.splitext(arquivo_nome)

    # Adicionar extensão .txt se necessário
    if not extensao:
      arquivo_nome = nome + ".txt"

    # Obter o diretório do código atual
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    # Construir o caminho completo do arquivo
    arquivo_completo = os.path.join(diretorio_atual, arquivo_nome)

    # Abrir o arquivo no modo de escrita ("w")
    with open(arquivo_completo, "w") as arquivo:
      # Escrever o conteúdo do campo de texto no arquivo
      arquivo.write(texto.get(1.0, tk.END))

    # Exibir mensagem de sucesso na interface
    mensagem_status.config(text=f"Texto salvo em '{arquivo_completo}'")

  except Exception as e:
    # Exibir mensagem de erro na interface
    mensagem_status.config(text=f"Erro ao salvar: {e}")
# Criar a janela principal
janela = tk.Tk()
janela.title("Salvar Texto em Arquivo:")

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