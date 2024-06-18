import tkinter as tk# Importa a biblioteca Tkinter para criar a interface gráfica.
from tkinter import messagebox# Importa a função messagebox do Tkinter para exibir caixas de diálogo.

# Dicionários com as opções e preços de pizza e ingredientes
tamanho_pizzas = ["Pequena", "Média", "Grande", "Família"]#Lista com os tamanhos de pizza disponíveis.
precos_pizzas = {"Pequena": 30, "Média": 50, "Grande": 70, "Família": 80}#Dicionário com os preços de cada tamanho de pizza.

ingredientes_adicionais = ["Catupiry", "Maionese caseira", "Ketchup", "Borda recheada"]#Lista com os ingredientes adicionais disponíveis.
precos_adicionais = {"Catupiry": 5, "Maionese caseira": 7, "Ketchup": 5, "Borda recheada": 10}#Dicionário com os preços de cada ingrediente adicional.

# Variáveis globais para armazenar o valor total e ingredientes selecionados
valor_total = 0# Armazena o valor total do pedido.
ingredientes_selecionados = []# Lista para armazenar os ingredientes

# Função para confirmar o pedido
def confirmar_pedido():
    global valor_total, ingredientes_selecionados, selecao_tamanho  # Declarar variáveis globais para acesso
    
    try:
        tamanho_selecionado1 = selecao_tamanho.get()
        quantidade = int(quantidade_pizzas.get())#int() converte o valor digitado no campo quantidade_pizzas em um número inteiro.
        if quantidade > 0 and tamanho_selecionado1 in precos_pizzas:#Se a conversão for bem-sucedida e a quantidade for maior que zero, prossegue para o próximo passo.
             tamanho = selecao_tamanho.get()#O valor selecionado no menu suspenso selecao_tamanho é armazenado na variável tamanho.
             valor_pizza = precos_pizzas[tamanho] * quantidade#O preço da pizza é calculado multiplicando o preço unitário do tamanho selecionado pela quantidade.
             valor_adicionais = sum(precos_adicionais[ingrediente] for ingrediente in ingredientes_selecionados)#Um loop percorre a lista ingredientes_selecionados.Para cada ingrediente, o preço é adicionado ao valor total.
             valor_total = valor_pizza + valor_adicionais#O valor total do pedido é a soma do valor da pizza e dos ingredientes adicionais.
             label_valor_total.config(text=f"Valor total: R$ {valor_total:.2f}")#O valor total é exibido na label label_valor_total.
             response = messagebox.askquestion("Confirmar Pedido",f"O valor total do seu pedido é de R$ {valor_total:.2f}. Deseja confirmar?")#Uma caixa de diálogo pergunta ao cliente se ele deseja confirmar o pedido.
             if response == "yes":#Se a resposta for "sim", prossegue para o próximo passo.
                    messagebox.showinfo("Pedido Confirmado", "Seu pedido foi enviado com sucesso!")#Uma mensagem informa que o pedido foi enviado com sucesso.

                    
                    print(f"Pedido confirmado: Tamanho: {selecao_tamanho.get()}, Quantidade: {quantidade_pizzas.get()},")
                    print(f"Ingredientes adicionais: {', '.join(ingredientes_selecionados)}")
                    print(f"Valor total: R$ {valor_total:.2f}")
                    label_valor_total.config(text=f"Valor total: R$ {valor_total:.2f}")

                   
                    # Percorra os elementos filhos do frame_ingredientes
                    for elemento_filho in frame_ingredientes.winfo_children():
                        # Verifique se o elemento filho é uma caixa de seleção (Checkbutton)
                        if isinstance(elemento_filho, tk.Checkbutton):
                             # Desmarque a caixa de seleção
                            elemento_filho.deselect()
                    
                    #As variáveis valor_total e ingredientes_selecionados são zeradas.   
                    #Os campos de entrada e a label do valor total são limpos.
                    valor_total = 0
                    label_valor_total.config(text="") 
                    quantidade_pizzas.delete(0, 'end')
                    selecao_tamanho.set("")
                    label_exibir_preco_unitario.config(text="")
             else:#Se a resposta da caixa de diálogo for "não", uma mensagem informa que o pedido foi cancelado.
                    messagebox.showinfo("Pedido Cancelado", "Seu pedido foi cancelado.")
                    for elemento_filho in frame_ingredientes.winfo_children():
                        # Verifique se o elemento filho é uma caixa de seleção (Checkbutton)
                        if isinstance(elemento_filho, tk.Checkbutton):
                             # Desmarque a caixa de seleção
                            elemento_filho.deselect()
                   #As variáveis valor_total e ingredientes_selecionados são zeradas.
                   #Os campos de entrada e a label do valor total são limpos.
                    valor_total = 0
                    label_valor_total.config(text="")
                    quantidade_pizzas.delete(0, 'end')
                    selecao_tamanho.set("")
                    label_exibir_preco_unitario.config(text="")
        
        else:#Se a conversão da quantidade falhar (valor não numérico ou menor que zero), uma mensagem de erro é exibida.
            raise ValueError("Quantidade inválida!")
    except ValueError:
        messagebox.showerror("Erro", "Quantidade inválida!")
        for elemento_filho in frame_ingredientes.winfo_children():
        # Verifique se o elemento filho é uma caixa de seleção (Checkbutton)
            if isinstance(elemento_filho, tk.Checkbutton):
                # Desmarque a caixa de seleção
                elemento_filho.deselect()
        #As variáveis valor_total e ingredientes_selecionados são zeradas.
        #Os campos de entrada e a label do valor total são limpos.
        valor_total = 0
        label_valor_total.config(text="")
        quantidade_pizzas.delete(0, 'end')
        selecao_tamanho.set("")
        label_exibir_preco_unitario.config(text="")
        return 
# Função para adicionar ou remover um ingrediente
def adicionar_ingrediente(ingrediente):#(ingrediente) O parâmetro da função, que representa o nome do ingrediente que está sendo passado para a função quando ela é chamada.
   
    global ingredientes_selecionados  # Declarar variável global para acesso

    if ingrediente in ingredientes_selecionados:#A condição verifica se o ingrediente (passado como parâmetro) está presente na lista ingredientes_selecionados.Se o ingrediente já estiver na lista, significa que ele deve ser removido.
        ingredientes_selecionados.remove(ingrediente)#remove(ingrediente): Este método remove o ingrediente especificado da lista ingredientes_selecionados.
    else:
        ingredientes_selecionados.append(ingrediente)#.append(ingrediente): Este método adiciona o ingrediente especificado à lista ingredientes_selecionados.

# Função para apresentar o valor unitário da pizza
def apresentar_valor_unitario(event=None):  # event: Este argumento aceita um evento, mas neste caso não é utilizado. Sua presença serve apenas para compatibilidade com o widget OptionMenu.
    
    global selecao_tamanho  # Declare a variável globalmente para garantir acessibilidade
    
    if selecao_tamanho.get():  # Uma variável global que armazena o tamanho da pizza selecionado pelo usuário.
        tamanho_selecionado = selecao_tamanho.get()
        if tamanho_selecionado in precos_pizzas:
            label_exibir_preco_unitario.config(text=f" Valor unitário: R$ {precos_pizzas[tamanho_selecionado]:.2f}")
        else:
            label_exibir_preco_unitario.config(text="Tamanho inválido!")
    else:
        # Opcional: Exibir mensagem informativa caso nenhum tamanho esteja selecionado
        label_exibir_preco_unitario.config(text="")


# Criação da interface gráfica
janela = tk.Tk()
janela.title("Pizza")
janela.geometry("200x400") # Define a largura como 200 pixels e a altura como 400 pixels.

# Frame para o título
frame_titulo = tk.Frame(janela)
frame_titulo.grid(row=1, column=0, columnspan=2, padx=10, pady=5)  # Linha acima do centro, coluna centralizada e abrangendo 2 colunas

# Título da tela
label_titulo = tk.Label(frame_titulo, text="Escolha o tamanho da Pizza:")
label_titulo.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

# Frame para seleção de tamanho e quantidade
frame_selecao = tk.Frame(janela)
frame_selecao.grid(row=2, column=0, columnspan=2, pady=10)

# Menu suspenso para selecionar o tamanho da pizza
selecao_tamanho = tk.StringVar(janela)
menu_pizzas = tk.OptionMenu(frame_selecao, selecao_tamanho, *tamanho_pizzas, command=apresentar_valor_unitario)
menu_pizzas.grid(row=0, column=0, padx=10, pady=5)

# Label para exibir o preço unitário
label_exibir_preco_unitario = tk.Label(frame_selecao, text="")
label_exibir_preco_unitario.grid(row=1, column=0, padx=10, pady=5)

# Campo de entrada para quantidade de pizzas
quantidade_pizzas = tk.Entry(frame_selecao)
quantidade_pizzas.grid(row=2, column=0, padx=10, pady=5)

# Frame para ingredientes adicionais
frame_ingredientes = tk.Frame(janela)
frame_ingredientes.grid(row=3, column=0, columnspan=2, pady=10)

for row, ingrediente in enumerate(ingredientes_adicionais):#Esta linha itera por uma lista chamada ingredientes_adicionais
    var = tk.IntVar()#Cria um objeto IntVar do tkinter. Esta variável armazenará o estado (marcado ou desmarcado) da caixa de seleção para cada ingrediente.
    l = tk.Checkbutton(frame_ingredientes, text=ingrediente, variable=var, command=lambda x=ingrediente: adicionar_ingrediente(x))#command=lambda x=ingrediente: adicionar_ingrediente(x): Define uma função anônima (lambda) que será executada quando a caixa de seleção for clicada. Esta função leva um argumento (x) que é automaticamente definido como o nome do ingrediente atual (ingrediente) devido à parte x=ingrediente. Dentro da função, ela chama outra função chamada adicionar_ingrediente (assumindo que esteja definida em outro lugar), passando o nome do ingrediente atual (x) como argumento. 
    l.grid(row=row, column=0, sticky="w", padx=10, pady=5)

# Frame para o botão de pedido e valor total
frame_valor = tk.Frame(janela)
frame_valor.grid(row=4, column=0, columnspan=2, pady=10)

# Botão para calcular o valor total
botao_pedido = tk.Button(frame_valor, text="Pedir", command=confirmar_pedido)
botao_pedido.grid(row=0, column=0, padx=10, pady=5)

# Label para exibir o valor total do pedido
label_valor_total = tk.Label(frame_valor, text="")
label_valor_total.grid(row=1, column=0, padx=10, pady=5)



# Execução da interface gráfica
janela.mainloop()