import tkinter as tk
from tkinter import ttk

#Exemplo de Uso > Quando o usuário executa o código, uma janela com o título "Menu de Café" é exibida. 
# O usuário pode escolher um tipo de café no menu de opções e clicar no botão "Escolher".
# O resultado da escolha é exibido no rótulo label_resultado.



def escolher_cafe():
    escolha = opcao_cafe.get()
    mensagem = f"Você escolheu: {escolha}"
    label_resultado.config(text=mensagem)

root = tk.Tk()
root.title("Menu de Café")

## Escolha de Café
label_cafe = tk.Label(root, text="Escolha seu café preferido:")
label_cafe.pack()

opcoes_cafe = ["Expresso", "Cappuccino", "Latte Macchiato"]
opcao_cafe = tk.StringVar()
opcao_cafe.set(opcoes_cafe[0])

menu_cafe = tk.OptionMenu(root, opcao_cafe, *opcoes_cafe)
menu_cafe.pack()

## Botão para escolher
botao_escolher = tk.Button(root, text="Escolher", command=escolher_cafe)
botao_escolher.pack()

## Exibir resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack()

root.mainloop() 

# Explicação:
# Passo 1 Importação de Bibliotecas
# Função escolher_cafe - A função escolher_cafe é definida para ser executada quando o botão "Escolher" é clicado. Essa função:
# Obtém o valor escolhido no menu de opções opcao_cafe usando o método get().
# Cria uma mensagem com o texto "Você escolheu: {escolha}", onde {escolha} é substituído pelo valor escolhido.
# Atualiza o texto do rótulo label_resultado com a mensagem criada.
# Criação da Janela
# A janela principal é criada com o comando root = tk.Tk(), que cria uma janela com o título "Menu de Café".
# Componentes da Janela  >>   Os componentes da janela são criados usando os widgets Tkinter:
# label_cafe: Um rótulo que exibe a mensagem "Escolha seu café preferido:".

# opcoes_cafe: Uma lista de opções que contém os tipos de café ("Expresso", "Cappuccino", "Latte Macchiato").
# opcao_cafe: Uma variável de string que armazena o valor escolhido no menu de opções.
#menu_cafe: Um menu de opções que exibe as opções de café.
# botao_escolher: Um botão que executa a função escolher_cafe quando clicado.
# label_resultado: Um rótulo que exibe o resultado da escolha do café.

# Componentes >>> Os componentes são organizados na janela usando o método pack(), que é um método de layout padrão em Tkinter. 
# componentes são dispostos verticalmente na 
# janela.

#Loop Principal
#O loop principal da janela é iniciado com o comando root.mainloop(), que permite que a janela interaja com o usuário.
#Função escolher_cafe
#A função escolher_cafe é executada quando o botão "Escolher" é clicado. Ela obtém o valor escolhido no menu de opções opcao_cafe e cria uma mensagem com o texto "Você escolheu: {escolha}", onde {escolha} é substituído pelo valor escolhido. Em seguida, ela atualiza o texto do rótulo label_resultado com a mensagem criada.
