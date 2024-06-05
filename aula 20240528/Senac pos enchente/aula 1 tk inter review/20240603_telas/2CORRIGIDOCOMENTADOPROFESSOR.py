# 2. Contar Letras:
# Crie uma função que conte o número de letras (A-Z, a-z) em um campo Text.
# Teste a função com diferentes textos, incluindo espaços em branco, números, pontuação e caracteres especiais.


import tkinter as tk
#importa a biblioteca Tkinter e a renomeia para tk. Isso permite que você use as classes e funções do Tkinter sem precisar escrever tkinter. antes de cada uma delas.


def contar_letras(texto):
  numero_letras = 0
  for c in texto:
    if c.isalpha():
      numero_letras += 1
  return numero_letras
#Afunção recebe uma string texto como argumento e retorna o número de letras maiúsculas e minúsculas que ela contém.
#A variável numero_letras é inicializada com 0 para armazenar a contagem de letras.
#O loop for percorre cada caractere no texto usando a variável c.
#Dentro do loop, a condição if c.isalpha() verifica se o caractere c é uma letra maiúscula ou minúscula usando a função isalpha().
#Se for uma letra, o valor de numero_letras é incrementado em 1.
#A contagem de letras é decrementada em 1 no final da função. 
#Isso ocorre porque o loop for conta o caractere de nova linha final (\n), que não deve ser considerado como uma letra.
#A função retorna o valor final de numero_letras, que representa a contagem de letras no texto.

# Cria a janela principal
janela = tk.Tk()
janela.title("Contar Letras")
#criam uma nova janela Tkinter e configuram seu título como "Contador de Caracteres". 
#A variável janela armazena uma referência à janela para que você possa manipulá-la posteriormente.


# Cria a caixa de entrada de texto
entrada_texto = tk.Text(janela)
entrada_texto.pack()
#Cria um widget Tkinter Text (campo de texto) e o empacota na janela principal. 

botao_contar_letras = tk.Button(janela, text="Contar Letras", command=lambda: resultado_label.config(text=f"O texto possui {contar_letras(entrada_texto.get(1.0, tk.END))} letras."))
botao_contar_letras.pack()
#Cria um widget Tkinter Button (botão) com o texto "Contar Letras". Quando o botão é clicado, a seguinte ação é executada:
#Uma função anônima (lambda) é chamada.
#Essa função obtém o texto do campo de entrada de texto usando entrada_texto.get(1.0, tk.END).
#Chama a função contar_letras para contar o número de letras no texto obtido.
#Atualiza o texto do rótulo resultado_label com a contagem de letras formatada como "O texto possui X letras.".

# Cria o rótulo para exibir o resultado
resultado_label = tk.Label(janela, text="")
resultado_label.pack()
#Cria um widget Tkinter Label (rótulo) com um texto vazio no início. O rótulo será usado para exibir a contagem de letras. O rótulo também é empacotado na janela principal.

# Executa a interface principal
janela.mainloop()
#inicia o loop principal da janela Tkinter. 
#Isso significa que a janela permanecerá aberta e responsiva a eventos do usuário até que você a feche manualmente.