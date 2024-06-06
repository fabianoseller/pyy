# 4 Carregar Texto de Arquivo:
# Crie uma função que permita ao usuário carregar o conteúdo de um arquivo de texto para o campo Text.
# Exiba o conteúdo do arquivo no campo Text.

import tkinter as tk#importa a biblioteca Tkinter e a renomeia para tk. Isso permite que você use as classes e funções do Tkinter sem precisar escrever tkinter. antes de cada uma delas.
import os#Importa o módulo os da biblioteca padrão do Python.
# O módulo os fornece diversas funções para interagir com o sistema operacional, como:
# Criar e gerenciar arquivos e diretórios
# Executar comandos do sistema operacional
# Obter informações do sistema
# Acessar variáveis de ambiente

def carregar_texto():
    try:
        arquivo_nome = caixa_entrada_nome_arquivo.get()#caixa_entrada_nome_arquivo.get() recupera o texto digitado no campo de entrada de nome do arquivo e o armazena na variável arquivo_nome.
        if not arquivo_nome:#Se arquivo_nome for vazio, uma exceção é lançada com a mensagem "Nome do arquivo inválido".
            raise Exception("Nome do arquivo inválido")

        # Obter o diretório do script
        diretorio_script = os.path.dirname(os.path.abspath(__file__))#os.path.dirname(os.path.abspath(__file__)) obtém o diretório do script Python atual e o armazena na variável diretorio_script.

        # Construir o caminho completo do arquivo
        arquivo_completo = os.path.join(diretorio_script, arquivo_nome)#os.path.join(diretorio_script, arquivo_nome) junta o diretório e o nome do arquivo para formar o caminho completo do arquivo e o armazena na variável arquivo_completo.

        if not os.path.exists(arquivo_completo):#os.path.exists(arquivo_completo) verifica se o arquivo especificado no caminho completo existe. Se não existir, uma exceção é lançada com a mensagem "Arquivo não encontrado".
            raise Exception("Arquivo não encontrado")

        if os.path.isdir(arquivo_completo):#s.path.isdir(arquivo_completo) verifica se o caminho especificado é um diretório. Se for um diretório, uma exceção é lançada com a mensagem "Caminho especificado é um diretório".
            raise Exception("Caminho especificado é um diretório")

        with open(arquivo_completo, "r") as arquivo:#O bloco with open(arquivo_completo, "r") as arquivo: abre o arquivo no modo de leitura ("r").
            texto.delete(1.0, tk.END)#A função texto.delete(1.0, tk.END) apaga todo o conteúdo existente no campo de texto texto.
            texto.insert(tk.END, arquivo.read())#A função texto.insert(tk.END, arquivo.read()) insere o conteúdo lido do arquivo no final do campo de texto texto.
            mensagem_status.config(text=f"Texto carregado de '{arquivo_completo}'")#A função mensagem_status.config(text=f"Texto carregado de '{arquivo_completo}'") exibe uma mensagem de sucesso na interface, informando o nome do arquivo carregado.

    except Exception as e:#Se qualquer erro ocorrer durante o processo de carregar o arquivo, a exceção é capturada na variável e.
        mensagem_status.config(text=f"Erro ao carregar: {e}")#A função mensagem_status.config(text=f"Erro ao carregar: {e}") exibe uma mensagem de erro na interface, informando a mensagem de erro da exceção.

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

# Criar área de texto para exibir a mensagem de status
mensagem_status = tk.Label(janela, text="")
mensagem_status.pack(pady=5)

# Executar o loop principal da interface
janela.mainloop()


