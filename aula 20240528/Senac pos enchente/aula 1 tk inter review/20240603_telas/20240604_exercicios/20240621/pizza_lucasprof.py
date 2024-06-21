from tkinter import *
import tkinter as tk# Importa a biblioteca Tkinter para criar a interface gráfica.
from tkinter import BOTH, messagebox# Importa a função messagebox do Tkinter para exibir caixas de diálogo.
import datetime
import mysql.connector
import re
from tkinter import ttk
cnx = mysql.connector.connect(host='127.0.0.1',user='root',password='')
from tkinter import Tk, Toplevel
# Executar a instrução SQL para verificar se o banco de dados existe
cursor = cnx.cursor()
cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "telepizza";')

# Obter o número de resultados
num_results = cursor.fetchone()[0]

# Fechar a conexão com o banco de dados
cnx.close()

# Se o número de resultados for maior que zero, o banco de dados existe
if num_results > 0:
  print('O banco de dados telepizza existe e esta pronto para uso.')
else:
    # Conectar-se ao servidor MySQL para criar o banco de dados
    cnx = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password=''
    )

    # Criar o banco de dados agenda
    cursor = cnx.cursor()
    cursor.execute('CREATE DATABASE telepizza;')
    cnx.commit()

    # Conectar-se ao banco de dados agenda recém-criado
    cnx = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='telepizza'  # Especificar o banco de dados
    )

    
    cursor = cnx.cursor()
    cursor.execute('CREATE TABLE pedidos (id INT AUTO_INCREMENT PRIMARY KEY, data DATE NOT NULL, tamanho VARCHAR(255),quantidade VARCHAR(255), valor_total DECIMAL(10,2) NOT NULL);')
    cursor.execute('CREATE TABLE clientes (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), telefone VARCHAR(255), email VARCHAR(255));')
    # Fechar a conexão com o banco de dados
    cnx.commit()
    cnx.close()
# Função para criar um novo pedido

def novo_pedido():
    # Dicionários com as opções e preços de pizza e ingredientes
    tamanho_pizzas = ["Pequena", "Média", "Grande", "Família"]#Lista com os tamanhos de pizza disponíveis.
    precos_pizzas = {"Pequena": 30, "Média": 50, "Grande": 70, "Família": 80}#Dicionário com os preços de cada tamanho de pizza.

    ingredientes_adicionais = ["Catupiry", "Maionese caseira", "Ketchup", "Borda recheada"]#Lista com os ingredientes adicionais disponíveis.
    precos_adicionais = {"Catupiry": 5, "Maionese caseira": 7, "Ketchup": 5, "Borda recheada": 10}#Dicionário com os preços de cada ingrediente adicional.

    # Variáveis globais para armazenar o valor total e ingredientes selecionados
    global valor_total,ingredientes_selecionados
    valor_total = 0# Armazena o valor total do pedido.
    ingredientes_selecionados = []# Lista para armazenar os ingrediente
    
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
                        cnx = mysql.connector.connect(
                        host='127.0.0.1',
                        user='root',
                        password='',
                        database='telepizza'
                        )
                    
                        cursor = cnx.cursor()
                        cursor.execute("INSERT INTO pedidos (data, tamanho, quantidade, valor_total) VALUES (%s, %s, %s, %s)", (datetime.datetime.now(), tamanho, quantidade, valor_total))
                        cnx.commit()
                        cnx.close()
                    
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
    global selecao_tamanho
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
def tela_addicinar_dados():
       
        janela_cadastro = Toplevel(janela_principal)
        janela_cadastro.title('Adicionar Cliente')

        # Entradas para adicionar dados
        nome_rotulo = tk.Label(janela_cadastro, text='Nome:')
        nome_rotulo.grid(row=0, column=0, padx=10, pady=10)
        nome_entrada =  tk.Entry(janela_cadastro)
        nome_entrada.grid(row=0, column=1, padx=10, pady=10)

        telefone_rotulo =  tk.Label(janela_cadastro, text='Telefone:')
        telefone_rotulo.grid(row=1, column=0, padx=10, pady=10)
        telefone_entrada =  tk.Entry(janela_cadastro)
        telefone_entrada.grid(row=1, column=1, padx=10, pady=10)
        
        
        

        email_rotulo =  tk.Label(janela_cadastro, text='Email:')
        email_rotulo.grid(row=2, column=0, padx=10, pady=10)
        email_entrada =  tk.Entry(janela_cadastro)
        email_entrada.grid(row=2, column=1, padx=10, pady=10)

        # Botão para confirmar a adição
        confirm_btn = tk.Button(janela_cadastro, text='Adicionar', command=lambda: addicinar_dados(nome_entrada.get(), telefone_entrada.get(), email_entrada.get(),janela_cadastro))
        confirm_btn.grid(row=3, column=0, columnspan=2, pady=10)
def addicinar_dados(nome, telefone, email,janela_cadastro):
         if nome == '' or telefone == '' or email == '':
            messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos.')
            return False

         if not re.match(r'^[0-9]+$', telefone):
            messagebox.showerror('Erro', 'O número de telefone deve conter apenas números.')
            return False

         if '@' not in email:
            messagebox.showerror('Erro', 'O e-mail deve conter um @.')
            return False

    # Adicionar dados ao banco de dados
         cnx = mysql.connector.connect(
                        host='127.0.0.1',
                        user='root',
                        password='',
                        database='telepizza'
                        )
                    
         cursor = cnx.cursor()
         cursor.execute('INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s)', (nome, telefone, email))
         cnx.commit()
         cnx.close()
         janela_cadastro.destroy()
def tela_clientes():
    janela_clientes =Toplevel(janela_principal)
    janela_clientes.title('Clientes')
    janela_clientes.focus_force()
         
    tabela = ttk.Treeview(janela_clientes, columns=('ID', 'Nome', 'Telefone', 'Email'), show='headings')
        
    tabela.heading('ID', text='ID')
    tabela.heading('Nome', text='Nome')
    tabela.heading('Telefone', text='Telefone')
    tabela.heading('Email', text='Email')
        
    tabela.pack(fill=BOTH, expand=True)
    tabela.bind('<Map>', lambda event: atualiza())
    def atualiza_cliente():
            if tabela.selection():
                # Janela para atualizar dados
               
                janela_cadastro = Toplevel(janela_clientes)
                janela_cadastro.title('Atualiza cliente')

                # Entradas para adicionar dados
                nome_rotulo = tk.Label(janela_cadastro, text='Nome:')
                nome_rotulo.grid(row=0, column=0, padx=10, pady=10)
                nome_entrada =  tk.Entry(janela_cadastro)
                nome_entrada.grid(row=0, column=1, padx=10, pady=10)

                telefone_rotulo =  tk.Label(janela_cadastro, text='Telefone:')
                telefone_rotulo.grid(row=1, column=0, padx=10, pady=10)
                telefone_entrada =  tk.Entry(janela_cadastro)
                telefone_entrada.grid(row=1, column=1, padx=10, pady=10)
                
                
                

                email_rotulo =  tk.Label(janela_cadastro, text='Email:')
                email_rotulo.grid(row=2, column=0, padx=10, pady=10)
                email_entrada =  tk.Entry(janela_cadastro)
                email_entrada.grid(row=2, column=1, padx=10, pady=10)

                # Botão para confirmar a adição
                confirm_btn = tk.Button(janela_cadastro, text='Adicionar', command=lambda: atualiza_banco(nome_entrada.get(), telefone_entrada.get(), email_entrada.get(),janela_cadastro))
                confirm_btn.grid(row=3, column=0, columnspan=2, pady=10)
                        
            else:
                # Nenhum item selecionado, mostre uma mensagem de erro ou faça outra ação
                messagebox.showerror('Erro', 'Nenhum registro selecionado.')
                return
    def atualiza_banco(novo_nome, novo_telefone, novo_email, janela_cadastro):
            if novo_nome == '' or novo_telefone == '' or novo_email == '':
                messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos.')
                return 

            if not re.match(r'^[0-9]+$', novo_telefone):
                messagebox.showerror('Erro', 'O número de telefone deve conter apenas números.')
                return 

            if '@' not in novo_email:
                messagebox.showerror('Erro', 'O e-mail deve conter um @.')
                return 
        
            item = tabela.selection()[0]
            data = tabela.item(item, 'values')
            id = data[0]
            # Atualizar dados no banco de dados
            # o objeto 'cursor' é utilizado para executar a instrução SQL
            cnx = mysql.connector.connect(
                            host='127.0.0.1',
                            user='root',
                            password='',
                            database='telepizza')
            # Buscar dados do banco de dados e popular a tabela treeview
            cursor = cnx.cursor()
            cursor.execute('UPDATE clientes SET nome=%s, telefone=%s, email=%s WHERE id=%s', (novo_nome, novo_telefone, novo_email, id))
            # Confirma a alteração no banco de dados usando a função commit
            cnx.commit()
            # Fecha a janela de atualização
            atualiza()
            janela_cadastro.destroy()
           
    def deleta_cliente():
                if tabela.selection():  # Verifica se há algum item selecionado
                    item = tabela.selection()[0]
                    # Pegar o ID do contato selecionado
                    data = tabela.item(item, 'values')
                    id = data[0]
        
            
            
                # Verificar se o usuário realmente deseja excluir o registro
                    if messagebox.askyesno('Confirmação', 'Tem certeza de que deseja excluir o registro?'):
                         
                    # Deletar dados do banco de dados
                        cnx = mysql.connector.connect(
                            host='127.0.0.1',
                            user='root',
                            password='',
                            database='telepizza')
            # Buscar dados do banco de dados e popular a tabela treeview
                        cursor = cnx.cursor()
                       
                        cursor.execute('DELETE FROM clientes WHERE id=%s', (id,))  # Passe o ID como uma tupla de um elemento
                        cnx.commit()
                        atualiza()
                        
                else:
            # Nenhum item selecionado, mostre uma mensagem de erro ou faça outra ação
                    messagebox.showerror('Erro', 'Nenhum registro selecionado.')
                    return
            
            
                # Obter o item selecionado   
    def atualiza():
        cnx = mysql.connector.connect(
                            host='127.0.0.1',
                            user='root',
                            password='',
                            database='telepizza')
            # Buscar dados do banco de dados e popular a tabela treeview
        cursor =  cursor = cnx.cursor()
        cursor.execute('SELECT * FROM clientes')
        rows = cursor.fetchall()

            # Limpar dados anteriores
        for row in tabela.get_children():
            tabela.delete(row)

            # Adicionar novos dados
        for row in rows:
            tabela.insert('', 'end', values=row)

            # Adicionar um evento de seleção
        tabela.bind('<<TreeviewSelect>>', selecao_unica)
            # Botões para atualizar e deletar
    def selecao_unica(event):
            # Obter o item selecionado
            item = tabela.selection()[0]

            # Pegar os dados do item selecionado
            data = tabela.item(item, 'values')
            id = data[0]
            nome = data[1]
            telefone = data[2]
            email = data[3]
            # Fazer algo com os dados
    botao_atualizar = tk.Button(janela_clientes, text="Atualizar", command=atualiza_cliente)
    botao_excluir = tk.Button(janela_clientes, text="Excluir", command=deleta_cliente)

    # Posicionando os botões lado a lado na mesma linha
    botao_atualizar.pack(side=LEFT) 
    botao_excluir.pack(side=LEFT) 
   
   

# Cria a janela principal
janela_principal = tk.Tk()

# Define o título da janela principal
janela_principal.title("Menu Principal")
janela_principal.geometry("400x200")
# Cria o menu principal
barra_de_menus = tk.Menu(janela_principal)

# Configura a janela principal para usar o menu criado
janela_principal.config(menu=barra_de_menus)

# Cria um menu suspenso com o rótulo "Cadastro"
menu_cadastro = tk.Menu(barra_de_menus, tearoff=0)

# Adiciona o menu "Cadastro" ao menu principal
barra_de_menus.add_cascade(label="Cadastro", menu=menu_cadastro)

# Adiciona uma opção "Cliente" ao menu "Cadastro"
menu_cadastro.add_command(label="Cliente", command=tela_addicinar_dados)

# Adiciona uma opção "Produto" ao menu "Cadastro"
menu_cadastro.add_command(label="Clientes", command=tela_clientes)

# Cria um menu suspenso com o rótulo "Pedido"
menu_pedido = tk.Menu(barra_de_menus, tearoff=0)

# Adiciona o menu "Pedido" ao menu principal
barra_de_menus.add_cascade(label="Pedido", menu=menu_pedido)

# Adiciona uma opção "Novo Pedido" ao menu "Pedido"
menu_pedido.add_command(label="Novo Pedido", command=novo_pedido)

# Adiciona uma opção "Consultar Pedidos" ao menu "Pedido"
menu_pedido.add_command(label="Consultar Pedidos", command=lambda: print("Consultando pedidos..."))

# Cria um menu suspenso com o rótulo "Relatório"
menu_relatorio = tk.Menu(barra_de_menus, tearoff=0)

# Adiciona o menu "Relatório" ao menu principal
barra_de_menus.add_cascade(label="Relatório", menu=menu_relatorio)

# Adiciona uma opção "Vendas por Período" ao menu "Relatório"
menu_relatorio.add_command(label="Vendas por Período", command=lambda: print("Gerando relatório de vendas por período..."))

# Adiciona uma opção "Produtos Mais Vendidos" ao menu "Relatório"
menu_relatorio.add_command(label="Produtos Mais Vendidos", command=lambda: print("Gerando relatório de produtos mais vendidos..."))

# Cria um menu suspenso com o rótulo "Configuração"
menu_configuracao = tk.Menu(barra_de_menus, tearoff=0)


janela_principal.mainloop()