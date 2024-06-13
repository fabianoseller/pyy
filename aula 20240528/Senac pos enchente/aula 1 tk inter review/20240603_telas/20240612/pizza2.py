import tkinter as tk
from tkinter import messagebox

# Dados da pizza
tamanhos = ["Pequena", "Média", "Grande"]
precos = {"Pequena": 15.00, "Média": 22.00, "Grande": 28.00}
ingredientes = ["Queijo Extra", "Pepperoni", "Bacon"]
precos_ingredientes = {"Queijo Extra": 2.00, "Pepperoni": 3.00, "Bacon": 4.00}

# Janela principal
root = tk.Tk()
root.title("Escolha o Tamanho da Pizza")

# Título
tk.Label(root, text="Escolha o Tamanho da Pizza").pack()

# Selecione o tamanho da pizza
var_tamanho = tk.StringVar()
var_tamanho.set(tamanhos[0])  # Default value
tk.OptionMenu(root, var_tamanho, *tamanhos).pack()

# Quantidade de pizzas
tk.Label(root, text="Quantidade de pizzas").pack()
quantidade = tk.Entry(root)
quantidade.pack()

# Ingredientes adicionais
tk.Label(root, text="Ingredientes adicionais").pack()
var_ingredientes = []
queijo_extra = tk.BooleanVar()
var_ingredientes.append(queijo_extra)
tk.Checkbutton(root, text="Queijo Extra", variable=queijo_extra).pack()

pepperoni = tk.BooleanVar()
var_ingredientes.append(pepperoni)
tk.Checkbutton(root, text="Pepperoni", variable=pepperoni).pack()

bacon = tk.BooleanVar()
var_ingredientes.append(bacon)
tk.Checkbutton(root, text="Bacon", variable=bacon).pack()

# Botão para pedir
def pedir():
    try:
        quantidade_valor = int(quantidade.get())
        if quantidade_valor < 0:
            messagebox.showerror("Erro", "Quantidade deve ser um número positivo.")
            return
    except ValueError:
        messagebox.showerror("Erro", "Quantidade deve ser um número.")
        return

    tamanho = var_tamanho.get()
    ingredientes_selecionados = [ingrediente for ingrediente, var in zip(ingredientes, var_ingredientes) if var.get()]
    preco_total = precos[tamanho] * quantidade_valor
    for ingrediente in ingredientes_selecionados:
        preco_total += precos_ingredientes[ingrediente]

    tk.Label(root, text=f"Total a pagar: R$ {preco_total:.2f}").pack()

    resposta = messagebox.askokcancel("Confirmação do Pedido", f"O total a pagar é R$ {preco_total:.2f}. Confirma o pedido?")
    if resposta:
        root.destroy()

tk.Button(root, text="Pedir", command=pedir).pack()

botao_sair = tk.Button(root, text="Sair", command=root.quit)
botao_sair.pack()

# Botão para mostrar detalhes do pedido
def mostrar_pedido():
    tamanho = var_tamanho.get()
    ingredientes_selecionados = [ingrediente for ingrediente, var in zip(ingredientes, var_ingredientes) if var.get()]
    preco_total = precos[tamanho]
    for ingrediente in ingredientes_selecionados:
        preco_total += precos_ingredientes[ingrediente]

    messagebox.showinfo("Detalhes do Pedido", f"Você pediu {quantidade} pizzas do tamanho {tamanho} com os ingredientes adicionais {', '.join(ingredientes_selecionados)}. O total ADICIONAL a pagar é R$ {preco_total:.2f}.")

botao_mostrar_pedido = tk.Button(root, text="Mostrar Pedido ADICIONAL", command=mostrar_pedido)
botao_mostrar_pedido.pack()

# Botão para cancelar pedidos
def cancelar_pedido():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

botao_cancelar = tk.Button(root, text="Cancelar", command=cancelar_pedido)
botao_cancelar.pack()
############
root.mainloop()


# #### explicando Aqui está uma lista explicando o código:

# 1. /  explicando / Importação de Bibliotecas/  explicando / :
#    - `import tkinter as tk`: Importa a biblioteca `tkinter` e a renomeia como `tk`.
#    - `from tkinter import messagebox`: Importa a classe `messagebox` da biblioteca `tkinter`.

# 2. /  explicando / Definição de Dados/  explicando / :
#    - `tamanhos = ["Pequena", "Média", "Grande"]`: Define uma lista com os tamanhos de pizza disponíveis.
#    - `precos = {"Pequena": 15.00, "Média": 22.00, "Grande": 28.00}`: Define um dicionário com os preços de cada tamanho de pizza.
#    - `ingredientes = ["Queijo Extra", "Pepperoni", "Bacon"]`: Define uma lista com os ingredientes adicionais disponíveis.
#    - `precos_ingredientes = {"Queijo Extra": 2.00, "Pepperoni": 3.00, "Bacon": 4.00}`: Define um dicionário com os preços de cada ingrediente adicional.

# 3. /  explicando / Criando a Janela Principal/  explicando / :
#    - `root = tk.Tk()`: Cria uma janela principal com o título "Escolha o Tamanho da Pizza".
#    - `root.title("Escolha o Tamanho da Pizza")`: Define o título da janela.

# 4. /  explicando / Criando Widgets/  explicando / :
#    - `tk.Label(root, text="Escolha o Tamanho da Pizza").pack()`: Cria um rótulo com o texto "Escolha o Tamanho da Pizza" e o adiciona à janela.
#    - `var_tamanho = tk.StringVar()`: Cria uma variável de string para armazenar o tamanho da pizza escolhido.
#    - `var_tamanho.set(tamanhos)`: Define o valor padrão da variável como o primeiro tamanho da lista.
#    - `tk.OptionMenu(root, var_tamanho, *tamanhos).pack()`: Cria um menu de opções com os tamanhos de pizza e o adiciona à janela.
#    - `tk.Label(root, text="Quantidade de pizzas").pack()`: Cria um rótulo com o texto "Quantidade de pizzas" e o adiciona à janela.
#    - `quantidade = tk.Entry(root)`: Cria um campo de entrada para a quantidade de pizzas.
#    - `quantidade.pack()`: Adiciona o campo de entrada à janela.
#    - `tk.Label(root, text="Ingredientes adicionais").pack()`: Cria um rótulo com o texto "Ingredientes adicionais" e o adiciona à janela.
#    - `var_ingredientes = []`: Cria uma lista para armazenar as variáveis de booleano para os ingredientes adicionais.
#    - `queijo_extra = tk.BooleanVar()`: Cria uma variável de booleano para o ingrediente "Queijo Extra".
#    - `var_ingredientes.append(queijo_extra)`: Adiciona a variável de booleano à lista.
#    - `tk.Checkbutton(root, text="Queijo Extra", variable=queijo_extra).pack()`: Cria um botão de seleção para o ingrediente "Queijo Extra" e o adiciona à janela.
#    - `pepperoni = tk.BooleanVar()`: Cria uma variável de booleano para o ingrediente "Pepperoni".
#    - `var_ingredientes.append(pepperoni)`: Adiciona a variável de booleano à lista.
#    - `tk.Checkbutton(root, text="Pepperoni", variable=pepperoni).pack()`: Cria um botão de seleção para o ingrediente "Pepperoni" e o adiciona à janela.
#    - `bacon = tk.BooleanVar()`: Cria uma variável de booleano para o ingrediente "Bacon".
#    - `var_ingredientes.append(bacon)`: Adiciona a variável de booleano à lista.
#    - `tk.Checkbutton(root, text="Bacon", variable=bacon).pack()`: Cria um botão de seleção para o ingrediente "Bacon" e o adiciona à janela.

# 5. /  explicando / Definição de Funções/  explicando / :
#    - `def pedir():`: Define uma função para processar o pedido.
#    - `def mostrar_pedido():`: Define uma função para mostrar detalhes do pedido.

# 6. /  explicando / Criando Botões/  explicando / :
#    - `tk.Button(root, text="Pedir", command=pedir).pack()`: Cria um botão com o texto "Pedir" e o adiciona à janela. O botão é associado à função `pedir`.
#    - `botao_sair = tk.Button(root, text="Sair", command=root.quit)`: Cria um botão com o texto "Sair" e o adiciona à janela. O botão é associado à função `quit` da janela.
#    - `botao_mostrar_pedido = tk.Button(root, text="Mostrar Pedido", command=mostrar_pedido)`: Cria um botão com o texto "Mostrar Pedido" e o adiciona à janela. O botão é associado à função `mostrar_pedido`.

# 7. /  explicando / Iniciando a Janela/  explicando / :
#    - `root.mainloop()`: Inicia a janela principal e começa a executar o loop principal da aplicação.