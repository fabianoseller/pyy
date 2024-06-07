import tkinter as tk
import os#Importa o módulo os da biblioteca padrão do Python.
# O módulo os fornece diversas funções para interagir com o sistema operacional, como:
# Criar e gerenciar arquivos e diretórios
# Executar comandos do sistema operacional
# Obter informações do sistema
# Acessar variáveis de ambiente
from tkinter import filedialog#Importa o módulo filedialog da biblioteca tkinter. Este módulo fornece funções para criar caixas de diálogo que permitem aos usuários selecionar arquivos ou diretórios.
def salvar_texto_carregado():
    try:
        # Verificar se há um arquivo carregado
        if not mensagem_status.cget("text").startswith("Texto carregado de "):
            raise Exception("Nenhum arquivo carregado para salvar")

        # Extrair o caminho do arquivo carregado da mensagem de status (sem aspas)
        caminho_arquivo = mensagem_status.cget("text")[18:].strip().split(".txt")[0].replace("'","")

        # Construir o nome do arquivo completo (sem aspas)
        arquivo_nome = f"{caminho_arquivo.strip()}.txt"

        # Abrir o arquivo no modo de escrita
        with open(arquivo_nome, "w") as arquivo:
            arquivo.write(texto.get(1.0, tk.END))

        # Atualizar a mensagem de status
        mensagem_status.config(text=f"Texto salvo em '{arquivo_nome}'")

    except Exception as e:
        mensagem_status.config(text=f"Erro ao salvar: {e}")
    
def salvar_texto():
    arquivo_nome = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivos de texto", "*.txt")],
    )
    #abre uma caixa de diálogo para que o usuário possa escolher um nome e local para salvar um arquivo.
# defaultextension=".txt": Define a extensão padrão do arquivo como ".txt".
# filetypes=[("Arquivos de texto", "*.txt")]: Limita a seleção de arquivos a arquivos de texto com a extensão ".txt".
    if arquivo_nome:
        # só será executado se o usuário escolher um nome e local para salvar o arquivo.
        try:
            #tenta abrir o arquivo para gravação e escrever o texto nele.
            with open(arquivo_nome, "w") as arquivo:
            #Abre o arquivo especificado por arquivo_nome no modo de escrita ("w").
            #O bloco de código dentro do with será executado com o arquivo aberto.
            #o modo de escrita "w" (abreviação de "write") se refere a um modo específico de abrir um arquivo para manipulação de dados.
          
                arquivo.write(texto.get(1.0, tk.END))
                #Lê o conteúdo da caixa de texto texto e escreve no arquivo aberto.
                #get(1.0, tk.END) recupera todo o texto da caixa de texto.
            mensagem_status.config(text=f"Texto salvo em '{arquivo_nome}'")
            #Atualiza o texto do rótulo mensagem_status para informar que o texto foi salvo com sucesso e o nome do arquivo.
        except Exception as e:
            mensagem_status.config(text=f"Erro ao salvar: {e}")
def limpar_texto():
   
    texto.delete(1.0, tk.END)# apaga todo o texto da caixa de texto texto.O método delete() recebe dois argumentos:1.0: Indica o início do texto a ser apagado (primeira linha, primeira coluna).tk.END: Indica o final do texto a ser apagado.
    mensagem_status.config(text="")#limpa a mensagem de status exibida no rótulo mensagem_status.O método config() é usado para configurar as propriedades do widget.No caso, a propriedade text é definida como uma string vazia (""), o que significa que a mensagem será removida.

def carregar_texto():
    
    try:# # Tenta executar o código dentro deste bloco. Se algo der errado, o bloco `except` será executado.
        arquivo_nome = filedialog.askopenfilename( # Abre uma janela para o usuário selecionar um arquivo de texto.# Retorna o nome do arquivo selecionado ou `None` se nenhum for selecionado.

            filetypes=[("Arquivos de texto", "*.txt")],
        )
        if arquivo_nome:# Se um arquivo foi selecionado...
            if not os.path.exists(arquivo_nome):
                raise Exception("Arquivo não encontrado")
             # Verifica se o arquivo existe.
      # Se não existir, levanta uma exceção com a mensagem "Arquivo não encontrado".


            if os.path.isdir(arquivo_nome):
                raise Exception("Caminho especificado é um diretório")
            # Verifica se o caminho selecionado é um diretório (pasta).
      # Se for um diretório, levanta uma exceção com a mensagem "Caminho especificado é um diretório".

            with open(arquivo_nome, "r") as arquivo:#O modo de escrita "r" (abreviação de "read") se refere a um modo específico de abrir um arquivo para leitura de dados. 
                 # Abre o arquivo no modo leitura ("r").
                 # O bloco `with` garante que o arquivo seja fechado automaticamente após o término do bloco.
                
                texto.delete(1.0, tk.END)
                # Apaga todo o conteúdo da caixa de texto `texto`.
                texto.insert(tk.END, arquivo.read())
                 # Insere o conteúdo do arquivo aberto na caixa de texto `texto`.
            mensagem_status.config(text=f"Texto carregado de '{arquivo_nome}'")
            # Atualiza a mensagem de status para informar que o Texto carregado de .
    except Exception as e:
        # Se algo der errado durante a execução do código dentro do bloco `try`, 
    # a exceção será capturada e armazenada na variável `e`.

        mensagem_status.config(text=f"Erro ao carregar: {e}")
        # Atualiza a mensagem de status para informar que ocorreu um erro e exibe a mensagem de erro capturada.


def contar_caracteres_e_letras(texto):#Esta função recebe um texto como entrada e retorna um dicionário contendo a contagem de linhas, caracteres e letras no texto.
  numero_linhas = len(texto.splitlines())#conta o número de linhas no texto.O método splitlines() divide o texto em uma lista de linhas com base nas quebras de linha (\n).A função len() conta o número de elementos na lista.O valor -1 é subtraído para remover a linha vazia que é criada no final do texto por splitlines().
  numero_caracteres = len(texto)-1#conta o número total de caracteres no texto.A função len() conta o número de caracteres na string texto.O valor -1 é subtraído para remover o caractere de quebra de linha (\n) no final do texto.
  numero_letras = 0#inicializa a variável numero_letras com 0, que será usada para contar o número de letras no texto.
  for c in texto:#Este loop percorre cada caractere no texto.A variável c recebe cada caractere do texto um por um.
    if c.isalpha():#Esta condição verifica se o caractere atual (c) é uma letra (maiúscula ou minúscula).O método isalpha() retorna True se o caractere for uma letra e False caso contrário.
      numero_letras += 1#Se o caractere atual for uma letra, o contador de letras (numero_letras) é incrementado em 1.

  return {"linhas": numero_linhas, "caracteres": numero_caracteres, "letras": numero_letras}#retorna um dicionário contendo os valores contados:linhas: O número de linhas no texto.caracteres: O número total de caracteres no texto.letras: O número de letras no texto.
def atualizar_resultado(dados):#Esta função recebe um dicionário contendo a contagem de linhas, caracteres e letras (dados) e atualiza o rótulo resultado_label com as informações de contagem.
  if dados['linhas']==0 and dados['letras']==0 and dados['caracteres']==0:#Esta condição verifica se todos os valores de contagem no dicionário dados são iguais a 0.Se todos os valores forem 0, significa que o texto está vazio ou não contém nenhum caractere.
      resultado_label.config(text="Não tenho o que contar")#Se o texto estiver vazio, o rótulo resultado_label é configurado com o texto "Não tenho o que contar".
  else:
      resultado_label.config(text=f"Linhas: {dados['linhas']}\nletras: {dados['letras']}\nCaracteres: {dados['caracteres']}")#Se o texto não estiver vazio, o bloco else será executado.
      #O rótulo resultado_label é configurado com um texto formatado contendo a contagem de linhas, letras e caracteres do texto.
      #As informações de contagem são obtidas do dicionário dados.
      #O caractere de nova linha (\n) é usado para separar as linhas de contagem no rótulo.


# Criar a janela principal
janela = tk.Tk()
janela.title("Criador de Arquivos TXT")

# Criar o widget Text
texto = tk.Text(janela, width=60, height=20)
texto.pack(pady=5)

# Criar frame para botões de salvar/carregar
frame_salvar_carregar = tk.Frame(janela)
frame_salvar_carregar.pack(pady=5)
# Adicionar botões ao frame usando grid
botao_salvar_texto_carregado = tk.Button(frame_salvar_carregar, text="Salvar", command=salvar_texto_carregado)
botao_salvar_texto_carregado.pack(pady=5)

#carregar Texto de Arquivo
botao_carregar_texto = tk.Button(frame_salvar_carregar, text="Carregar Texto", command=carregar_texto)
botao_carregar_texto.pack(pady=5)

# Criar frame para botões de contagem
frame_contar = tk.Frame(janela)
frame_contar.pack(pady=5)

# Adicionar botões ao frame usando grid
botao_limpar_texto = tk.Button(frame_contar, text="Limpar Texto", command=limpar_texto)
botao_limpar_texto.pack(pady=5)

botao_contar_caracteres = tk.Button(frame_contar, text="Contar Tudo", command=lambda: atualizar_resultado(contar_caracteres_e_letras(texto.get(1.0, tk.END))))
#cria um widget Button usando o módulo tkinter.
#O botão é criado dentro do frame frame_contar.
#O texto do botão é definido como "Contar Tudo".
# O commad define a função que será executada quando o botão for clicado.
# atualizar_resultado é a função que será chamada.
# contar_caracteres_e_letras(texto.get(1.0, tk.END)) é o argumento que será passado para a função atualizar_resultado.
#texto.get(1.0, tk.END) obtém todo o texto da caixa de texto texto
botao_contar_caracteres.pack(pady=5)


# Adicionar botões ao frame usando grid
botao_salvar_texto = tk.Button(frame_salvar_carregar, text="Criar novo arquivo", command=salvar_texto)
botao_salvar_texto.pack(pady=5)







# Criar área de texto para exibir a mensagem de status
mensagem_status = tk.Label(janela, text="")
mensagem_status.pack(pady=5)
resultado_label = tk.Label(janela, text="")
resultado_label.pack(pady=5)

# Executar o loop p
# Executar o loop principal da interface
janela.mainloop()