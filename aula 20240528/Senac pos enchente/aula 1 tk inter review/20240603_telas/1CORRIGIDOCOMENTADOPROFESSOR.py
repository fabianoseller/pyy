# 1. Contar Caracteres:
# Crie uma função que conte o número de caracteres (incluindo espaços) em um campo Text.
# Teste a função com diferentes textos, incluindo espaços em branco e caracteres especiais.


import tkinter as tk
#importa a biblioteca Tkinter e a renomeia para tk. Isso permite que você use as classes e funções do Tkinter sem precisar escrever tkinter. antes de cada uma delas.

def contar_caracteres():
    texto = entrada_texto.get(1.0, tk.END)
    numero_caracteres = len(texto) - 1
    resultado_label.config(text=f"O texto possui {numero_caracteres} caracteres.")
#Quando o botão "Contar Caracteres" é clicado. Ela faz o seguinte:Obtém o conteúdo do campo de texto entrada_texto usando o método get(1.0, tk.END). 
#Isso significa que obtém todo o texto do campo, desde o início (índice 1.0) até o final (índice tk.END).
#Conta o número de caracteres no texto usando a função len e subtrai 1 para remover o caractere de nova linha final.
#Atualiza o texto do rótulo resultado_label para mostrar a contagem de caracteres formatada com a frase "O texto possui X caracteres.".

# Cria a janela principal
janela = tk.Tk()
janela.title("Contador de Caracteres")
#criam uma nova janela Tkinter e configuram seu título como "Contador de Caracteres". 
#A variável janela armazena uma referência à janela para que você possa manipulá-la posteriormente.

# Cria a caixa de entrada de texto
entrada_texto = tk.Text(janela)
entrada_texto.pack()
#Cria um widget Tkinter Text (campo de texto) e o empacota na janela principal. 


# Cria botão para contar caracteres 
botao_contar_caracteres = tk.Button(janela, text="Contar Caracteres", command=contar_caracteres)
botao_contar_caracteres.pack()
#cria um widget Tkinter Button (botão) com o texto "Contar Caracteres". 
#Quando o botão é clicado, a função contar_caracteres é chamada. 


# Cria o rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()
#Cria um widget Tkinter Label (rótulo) com um texto vazio no início. 
#O rótulo será usado para exibir a contagem de caracteres. 


janela.mainloop()
#inicia o loop principal da janela Tkinter. 
#Isso significa que a janela permanecerá aberta e responsiva a eventos do usuário até que você a feche manualmente.