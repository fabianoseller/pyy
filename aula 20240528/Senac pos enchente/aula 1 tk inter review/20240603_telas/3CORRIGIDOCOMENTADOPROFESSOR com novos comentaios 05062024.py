# 3 Salvar Texto em Arquivo:
# Crie uma função que permita ao usuário salvar o conteúdo do campo Text em um arquivo de texto.
# Exiba uma mensagem de sucesso ou erro após a operação.

import tkinter as tk
#importa a biblioteca Tkinter e a renomeia para tk. Isso permite que você use as classes e funções do Tkinter sem precisar escrever tkinter. antes de cada uma delas.
import os
# Importa o módulo os da biblioteca padrão do Python.
# O módulo os fornece diversas funções para interagir com o sistema operacional, como:
# Criar e gerenciar arquivos e diretórios
# Executar comandos do sistema operacional
# Obter informações do sistema
# Acessar variáveis de ambiente




def salvar_texto():#Essa função é responsável por salvar o conteúdo do campo de texto em um arquivo
  try:# bloco try-except para lidar com possíveis erros durante o processo de salvar o arquivo.
    
    # Obter o nome do arquivo do campo de entrada
    arquivo_nome = caixa_entrada_nome_arquivo.get()#A caixa_entrada_nome_arquivo.get() recupera o texto digitado no campo de entrada de nome do arquivo e o armazena na variável arquivo_nome.

    # Validar o nome do arquivo
    if not arquivo_nome:
      raise Exception("Nome do arquivo inválido")#Se arquivo_nome for vazio, uma exceção é lançada com a mensagem

    # Separar nome e extensão (se houver)
    nome, extensao = os.path.splitext(arquivo_nome)# os.path.splitext(arquivo_nome) divide o nome do arquivo em nome e extensão.

    # Adicionar extensão .txt se necessário
    if not extensao:
      arquivo_nome = nome + ".txt"#Se a extensão não existir,  adiciona ".txt" ao nome do arquivo.

    # Obter o diretório do código atual
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))# os.path.dirname(os.path.abspath(__file__)) obtém o diretório do script Python atual.

    # Construir o caminho completo do arquivo
    arquivo_completo = os.path.join(diretorio_atual, arquivo_nome)# os.path.join() junta o diretório e o nome do arquivo para formar o caminho completo do arquivo.

    # Abrir o arquivo no modo de escrita ("w")
    with open(arquivo_completo, "w") as arquivo:#O bloco with open(arquivo_completo, "w") as arquivo: abre o arquivo no modo de escrita ("w").
      # Escrever o conteúdo do campo de texto no arquivo
      arquivo.write(texto.get(1.0, tk.END))# arquivo.write(texto.get(1.0, tk.END)) escreve o conteúdo do campo de texto  no arquivo aberto.

    # Exibir mensagem de sucesso na interface
    mensagem_status.config(text=f"Texto salvo em '{arquivo_completo}'")# mensagem_status.config(text=f"Texto salvo em '{arquivo_completo}'") exibe uma mensagem de sucesso na interface, informando o nome do arquivo salvo.

  except Exception as e:#Se qualquer erro ocorrer durante o processo de salvar, a exceção é capturada na variável e.
    # Exibir mensagem de erro na interface
    mensagem_status.config(text=f"Erro ao salvar: {e}")# mensagem_status.config(text=f"Erro ao salvar: {e}") exibe uma mensagem de erro na interface, informando a mensagem de erro da exceção.
# Criar a janela principal
janela = tk.Tk()# tk.Tk() cria a janela principal da interface gráfica e a armazena na variável janela.
janela.title("Salvar Texto em Arquivo:")# janela.title("Salvar Texto em Arquivo:") define o título da janela.

# Criar o widget Text
texto = tk.Text(janela, width=60, height=20)# tk.Text(janela, width=60, height=20) cria um campo de texto multiline na janela, com largura 60 e altura 20 caracteres.
texto.pack(padx=10, pady=10)# texto.pack(padx=10, pady=10) posiciona o campo de texto na janela com um padding de 10 pixels em todas as direções.

# Criar área de entrada para nome do arquivo
caixa_entrada_nome_arquivo = tk.Entry(janela)# tk.Entry(janela) cria um campo de entrada de texto na janela.
caixa_entrada_nome_arquivo.pack(pady=5)# caixa_entrada_nome_arquivo.pack(pady=5) posiciona o campo de entrada na janela com um padding de 5 pixels na parte superior.

# Criar botão para salvar texto
botao_salvar_texto = tk.Button(janela, text="Salvar Texto", command=salvar_texto)#tk.Button(janela, text="Salvar Texto", command=salvar_texto) cria um botão na janela com o texto "Salvar Texto".
botao_salvar_texto.pack(pady=5)#O parâmetro command=salvar_texto especifica que salvar_texto deve ser executada quando o botão for clicado
# botao_salvar_texto.pack(pady=5) posiciona o botão na janela com um padding de 5 pixels na parte superior.

# Criar área de texto para exibir a mensagem de status
mensagem_status = tk.Label(janela, text="")#tk.Label(janela, text="") cria uma área de texto na janela para exibir mensagens.
mensagem_status.pack(pady=5)#mensagem_status.pack(pady=5) posiciona a área de mensagem na janela com um padding de 5 pixels na parte superior.

# Executar o loop principal da interface
janela.mainloop()