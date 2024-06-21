import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class FormularioCliente:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Cadastro de Clientes")
        self.janela.geometry("800x600")

        # Criar rótulos e campos de entrada
        self.rotulo_nome = tk.Label(janela, text="Nome:")
        self.rotulo_nome.grid(row=0, column=0)
        self.campo_nome = tk.Entry(janela, width=40)
        self.campo_nome.grid(row=0, column=1)

        self.rotulo_email = tk.Label(janela, text="E-mail:")
        self.rotulo_email.grid(row=1, column=0)
        self.campo_email = tk.Entry(janela, width=40)
        self.campo_email.grid(row=1, column=1)

        self.rotulo_telefone = tk.Label(janela, text="Telefone:")
        self.rotulo_telefone.grid(row=2, column=0)
        self.campo_telefone = tk.Entry(janela, width=40)
        self.campo_telefone.grid(row=2, column=1)

        self.rotulo_endereco = tk.Label(janela, text="Endereço:")
        self.rotulo_endereco.grid(row=3, column=0)
        self.campo_endereco = tk.Text(janela, width=80, height=3)
        self.campo_endereco.grid(row=3, column=1)

        # Botões para as operações CRUD
        self.botao_salvar = tk.Button(janela, text="Salvar", command=self.salvar_cliente)
        self.botao_salvar.grid(row=4, column=0)
        self.botao_atualizar = tk.Button(janela, text="Atualizar", command=self.atualizar_cliente)
        self.botao_atualizar.grid(row=4, column=1)
        self.botao_excluir = tk.Button(janela, text="Excluir", command=self.excluir_cliente)
        self.botao_excluir.grid(row=4, column=2)

        # Tabela para exibir os clientes cadastrados
        self.tabela_clientes = ttk.Treeview(janela, columns=("client_id", "nome", "endereco", "telefone", "email"), show="headings")
        self.tabela_clientes.grid(row=5, column=0, columnspan=3)
        self.tabela_clientes.heading("client_id", text="ID")
        self.tabela_clientes.heading("nome", text="Nome")
        self.tabela_clientes.heading("endereco", text="Endereço")
        self.tabela_clientes.heading("telefone", text="Telefone")
        self.tabela_clientes.heading("email", text="E-mail")

        self.carregar_clientes()

    def carregar_clientes(self):
        # Carregar os clientes do banco de dados e exibir na tabela
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='pizzasnachtech'
        )
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM clientes")
        for linha in cursor:
            self.tabela_clientes.insert("", "end", values=linha)
        cursor.close()
        conexao.close()

        # Mostrar mensagem de confirmação
        messagebox.showinfo("Atualização realizada com sucesso!")

    def salvar_cliente(self):
        # Validar o campo de email
        if "@" not in self.campo_email.get():
            messagebox.showerror("Erro", "Deve conter arroba@ no email, por favor.")
            return

        # Salvar o cliente no banco de dados
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='pizzasnachtech'
        )
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO clientes (nome, endereco, telefone, email) VALUES (%s, %s, %s, %s)", (self.campo_nome.get(), self.campo_endereco.get("1.0", tk.END).strip(), self.campo_telefone.get(), self.campo_email.get()))
        conexao.commit()
        cursor.close()
        conexao.close()

        # Adicionar o cliente à tabela
        self.tabela_clientes.insert("", "end", values=(None, self.campo_nome.get(), self.campo_endereco.get("1.0", tk.END).strip(), self.campo_telefone.get(), self.campo_email.get()))

        # Limpar os campos de entrada
        self.campo_nome.delete(0, tk.END)
        self.campo_email.delete(0, tk.END)
        self.campo_telefone.delete(0, tk.END)
        self.campo_endereco.delete("1.0", tk.END)

        # Mostrar mensagem de confirmação
        messagebox.showinfo("Atualização realizada com sucesso!")

    def atualizar_cliente(self):
        # Obter o item selecionado na tabela
        item_selecionado = self.tabela_clientes.focus()
        if not item_selecionado:
            messagebox.showerror("Erro", "Selecione um cliente para atualizar.")
            return

        # Obter os valores atuais do cliente selecionado
        valores = self.tabela_clientes.item(item_selecionado, "values")
        self.campo_nome.delete(0, tk.END)
        self.campo_nome.insert(0, valores[1])
        self.campo_email.delete(0, tk.END)
        self.campo_email.insert(0, valores[4])
        self.campo_telefone.delete(0, tk.END)
        self.campo_telefone.insert(0, valores[3])
        self.campo_endereco.delete("1.0", tk.END)
        self.campo_endereco.insert("1.0", valores[2])

        # Atualizar o cliente no banco de dados
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='pizzasnachtech'
        )
        cursor = conexao.cursor()
        cursor.execute("UPDATE clientes SET nome=%s, endereco=%s, telefone=%s, email=%s WHERE email=%s", (self.campo_nome.get(), self.campo_endereco.get("1.0", tk.END).strip(), self.campo_telefone.get(), self.campo_email.get(), valores[4]))
        conexao.commit()
        cursor.close()
        conexao.close()

        # Atualizar a tabela
        self.tabela_clientes.item(item_selecionado, values=(valores[0], self.campo_nome.get(), self.campo_endereco.get("1.0", tk.END).strip(), self.campo_telefone.get(), self.campo_email.get()))

        # Mostrar mensagem de confirmação
        messagebox.showinfo("Atualização realizada com sucesso!")

    def excluir_cliente(self):
        # Obter o item selecionado na tabela
        item_selecionado = self.tabela_clientes.focus()
        if not item_selecionado:
            messagebox.showerror("Erro", "Selecione um cliente para excluir.")
            return

        # Perguntar se o usuário tem certeza que quer excluir o cliente
        valores = self.tabela_clientes.item(item_selecionado, "values")
        if messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir o cliente {valores[1]}?"):
            # Excluir o cliente do banco de dados
            conexao = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='pizzasnachtech'
            )
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM clientes WHERE email=%s", (valores[4],))
            conexao.commit()
            cursor.close()
            conexao.close()

            # Remover o cliente da tabela
            self.tabela_clientes.delete(item_selecionado)

            # Mostrar mensagem de confirmação
            messagebox.showinfo("Exclusão realizada com sucesso!")

janela = tk.Tk()
formulario_cliente = FormularioCliente(janela)
janela.mainloop()
