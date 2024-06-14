import tkinter as tk
from tkinter import messagebox

def padx_explicacao():
    nova_janela = tk.Toplevel(root)
    nova_janela.title('padx')

    # Título
    conteudo_label = tk.Label(nova_janela, text="padx:", font=("Arial", 10, "bold"))
    conteudo_label.grid(row=0, column=0, padx=20)

    # Exemplo
    conteudo_label = tk.Label(nova_janela, text="Exemplo:", font=("Arial", 10, "bold"))
    conteudo_label.grid(row=1, column=0, padx=20)

    # Explicação
    conteudo_label = tk.Label(nova_janela, text="label2.grid(row=1, column=0, padx=20)")
    conteudo_label.grid(row=2, column=0, padx=20)

def sticky_explicacao():
    nova_janela = tk.Toplevel(root)
    nova_janela.title('sticky')

    # Título
    conteudo_label = tk.Label(nova_janela, text="sticky:", font=("Arial", 10, "bold"))
    conteudo_label.pack()

    # Exemplo
    conteudo_label = tk.Label(nova_janela, text="Exemplo:", font=("Arial", 10, "bold"))
    conteudo_label.pack()

    # Explicação
    conteudo_label = tk.Label(nova_janela, text="botao1.grid(row=0, column=0, sticky=tk.N)")
    conteudo_label.pack()

# Dados da pizza
tamanhos = ["Pequena", "Média", "Grande"]
precos = {"Pequena": 15.00, "Média": 22.00, "Grande": 28.00}
ingredientes = ["Queijo Extra", "Pepperoni", "Bacon"]
precos_ingredientes = {"Queijo Extra": 2.00, "Pepperoni": 3.00, "Bacon": 4.00}

# Janela principal
root = tk.Tk()
root.title("Escolha o Tamanho da Pizza")

# Título
tk.Label(root, text="Escolha o Tamanho da Pizza").grid(row=0, column=0, columnspan=2, pady=10)

# Selecione o tamanho da pizza
tk.Label(root, text="Tamanho da Pizza:").grid(row=1, column=0, padx=10, pady=5)
var_tamanho = tk.StringVar()
var_tamanho.set(tamanhos[0])
tk.OptionMenu(root, var_tamanho, *tamanhos).grid(row=1, column=1, padx=10, pady=5)

# Quantidade de pizzas
tk.Label(root, text="Quantidade de Pizzas:").grid(row=2, column=0, padx=10, pady=5)
quantidade = tk.Entry(root)
quantidade.grid(row=2, column=1, padx=10, pady=5)

# Ingredientes adicionais
tk.Label(root, text="Ingredientes Adicionais:").grid(row=3, column=0, padx=10, pady=5)
var_ingredientes = []
queijo_extra = tk.BooleanVar()
var_ingredientes.append(queijo_extra)
tk.Checkbutton(root, text="Queijo Extra", variable=queijo_extra).grid(row=3, column=1, padx=10, pady=5)

pepperoni = tk.BooleanVar()
var_ingredientes.append(pepperoni)
tk.Checkbutton(root, text="Pepperoni", variable=pepperoni).grid(row=4, column=1, padx=10, pady=5)

bacon = tk.BooleanVar()
var_ingredientes.append(bacon)
tk.Checkbutton(root, text="Bacon", variable=bacon).grid(row=5, column=1, padx=10, pady=5)

# Configura o tamanho das linhas
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
#  parâmetro sticky no método grid() para especificar que o botão deve ser alinhado à direita da célula. Isso garantirá que o valor preenchido seja mostrado corretamente abaixo da frase "Total a pagar".
# Este código cria uma janela com opções para escolher o tamanho da pizza, quantidade de pizzas e ingredientes adicionais. Quando o botão "Pedir" é clicado, o código calcula o total a pagar 
#e solicita confirmação do pedido. Se o pedido for confirmado, a janela é fechada. O botão "Mostrar Pedido ADICIONAL" exibe detalhes do pedido, e o botão "Cancelar" remove todos os widgets da janela.
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

    tk.Label(root, text=f"Total a pagar: R$ {preco_total:.2f}").grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    resposta = messagebox.askokcancel("Confirmação do Pedido", f"O total a pagar é R$ {preco_total:.2f}. Confirma o pedido?")
    if resposta:
        root.destroy()

tk.Button(root, text="Pedir", command=pedir).grid(row=6, column=0, padx=10, pady=10)

# Botão para mostrar detalhes do pedido
def mostrar_pedido():
    tamanho = var_tamanho.get()
    ingredientes_selecionados = [ingrediente for ingrediente, var in zip(ingredientes, var_ingredientes) if var.get()]
    preco_total = precos[tamanho]
    for ingrediente in ingredientes_selecionados:
        preco_total += precos_ingredientes[ingrediente]

    messagebox.showinfo("Detalhes do Pedido", f"Você pediu {quantidade} pizzas do tamanho {tamanho} com os ingredientes adicionais {', '.join(ingredientes_selecionados)}. O total a pagar é R$ {preco_total:.2f}.")

tk.Button(root, text="Mostrar Pedido ADICIONAL", command=mostrar_pedido).grid(row=6, column=1, padx=10, pady=10)

# Botão para cancelar pedidos
def cancelar_pedido():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

tk.Button(root, text="Cancelar", command=cancelar_pedido).grid(row=7, column=0, columnspan=2, padx=10, pady=10)
# Configura o tamanho das linhas
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

tk.Button(root, text="Pedir", command=pedir).grid(row=6, column=0, padx=10, pady=10, sticky=tk.E)

root.mainloop()