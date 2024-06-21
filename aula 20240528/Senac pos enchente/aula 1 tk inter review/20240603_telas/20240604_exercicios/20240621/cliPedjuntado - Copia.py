import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

class PizzariaTech(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PizzariaTech")

        # Criar o menu principal
        self.menubar = tk.Menu(self)
        self.config(menu=self.menubar)

        # Criar o submenu "Cadastro"
        self.cadastro_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Cadastro", menu=self.cadastro_menu)
        self.cadastro_menu.add_command(label="Clientes", command=self.show_client_form)
        self.cadastro_menu.add_command(label="Voltar", command=self.hide_client_form)

        # Criar o submenu "Pedido"
        self.pedido_menu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label="Pedido", menu=self.pedido_menu)
        self.pedido_menu.add_command(label="Pedidos", command=self.show_order_form)
        self.pedido_menu.add_command(label="Voltar", command=self.hide_order_form)

        # Criar o submenu "Sair"
        self.menubar.add_command(label="Sair", command=self.quit)

        # Inicializar as janelas de cadastro
        self.client_form = None
        self.order_form = None

    def show_client_form(self):
        if self.client_form is None:
            self.client_form = ClientForm(self)
            self.client_form.grid(row=0, column=0, padx=20, pady=20)
        else:
            self.client_form.tkraise()

    def hide_client_form(self):
        if self.client_form is not None:
            self.client_form.grid_forget()
            self.client_form = None

    def show_order_form(self):
        if self.order_form is None:
            self.order_form = OrderForm(self)
            self.order_form.grid(row=0, column=0, padx=20, pady=20)
        else:
            self.order_form.tkraise()

    def hide_order_form(self):
        if self.order_form is not None:
            self.order_form.grid_forget()
            self.order_form = None

class ClientForm(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Criar labels e entrys para os campos de entrada
        self.email_label = tk.Label(self, text="E-mail:")
        self.email_label.grid(row=0, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(self, width=40)
        self.email_entry.grid(row=0, column=1, padx=10, pady=10)

        self.nome_label = tk.Label(self, text="Nome:")
        self.nome_label.grid(row=1, column=0, padx=10, pady=10)
        self.nome_entry = tk.Entry(self, width=40)
        self.nome_entry.grid(row=1, column=1, padx=10, pady=10)

        self.endereco_label = tk.Label(self, text="Endereço:")
        self.endereco_label.grid(row=2, column=0, padx=10, pady=10)
        self.endereco_entry = tk.Entry(self, width=40)
        self.endereco_entry.grid(row=2, column=1, padx=10, pady=10)

        self.telefone_label = tk.Label(self, text="Telefone:")
        self.telefone_label.grid(row=3, column=0, padx=10, pady=10)
        self.telefone_entry = tk.Entry(self, width=40)
        self.telefone_entry.grid(row=3, column=1, padx=10, pady=10)

        # Botões
        self.save_button = tk.Button(self, text="Salvar", command=self.save_client)
        self.save_button.grid(row=4, column=0, padx=10, pady=10)
        self.back_button = tk.Button(self, text="Voltar", command=self.master.hide_client_form)
        self.back_button.grid(row=4, column=1, padx=10, pady=10)

        # Tabela para exibir os clientes cadastrados
        self.client_table = ttk.Treeview(self, columns=("cliente_id", "email", "nome", "endereco", "telefone"), show="headings")
        self.client_table.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.client_table.heading("cliente_id", text="ID")
        self.client_table.heading("email", text="E-mail")
        self.client_table.heading("nome", text="Nome")
        self.client_table.heading("endereco", text="Endereço")
        self.client_table.heading("telefone", text="Telefone")

        # Carregar dados do banco de dados
        self.load_data()

    def save_client(self):
        # Verificar se os campos foram preenchidos
        if not self.email_entry.get() or not self.nome_entry.get() or not self.endereco_entry.get() or not self.telefone_entry.get():
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        # Criar um novo cliente com os dados inseridos
        client = {
            "email": self.email_entry.get(),
            "nome": self.nome_entry.get(),
            "endereco": self.endereco_entry.get(),
            "telefone": self.telefone_entry.get()
        }

        try:
            # Salvar o cliente no banco de dados
            cnx = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='pizzasnachtech'
            )
            cursor = cnx.cursor()
            cursor.execute("INSERT INTO clientes (email, nome, endereco, telefone) VALUES (%s, %s, %s, %s)",
                           (client["email"], client["nome"], client["endereco"], client["telefone"]))
            cnx.commit()
            client_id = cursor.lastrowid
            cursor.close()
            cnx.close()

            # Adicionar o cliente à tabela
            self.client_table.insert("", "end", values=(client_id, client["email"], client["nome"], client["endereco"], client["telefone"]))

            # Limpar os campos de entrada
            self.email_entry.delete(0, tk.END)
            self.nome_entry.delete(0, tk.END)
            self.endereco_entry.delete(0, tk.END)
            self.telefone_entry.delete(0, tk.END)
        except mysql.connector.Error as err:
            messagebox.showerror("Erro de Banco de Dados", f"Erro: {err}")

    def load_data(self):
        try:
            # Conectar ao banco de dados
            cnx = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='pizzasnachtech'
            )
            cursor = cnx.cursor()
            cursor.execute("SELECT cliente_id, email, nome, endereco, telefone FROM clientes")
            clientes = cursor.fetchall()
            cursor.close()
            cnx.close()

            # Adicionar dados à tabela
            for cliente in clientes:
                self.client_table.insert("", "end", values=cliente)
        except mysql.connector.Error as err:
            messagebox.showerror("Erro de Banco de Dados", f"Erro: {err}")

class OrderForm(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Criar labels e entrys para os campos de entrada
        self.client_id_label = tk.Label(self, text="Cliente ID:")
        self.client_id_label.grid(row=0, column=0, padx=10, pady=10)
        self.client_id_entry = tk.Entry(self, width=40)
        self.client_id_entry.grid(row=0, column=1, padx=10, pady=10)

        self.datetime_label = tk.Label(self, text="Data/Hora do Pedido:")
        self.datetime_label.grid(row=1, column=0, padx=10, pady=10)
        self.datetime_entry = tk.Entry(self, width=40)
        self.datetime_entry.grid(row=1, column=1, padx=10, pady=10)

        self.payment_label = tk.Label(self, text="Forma de Pagamento:")
        self.payment_label.grid(row=2, column=0, padx=10, pady=10)
        self.payment_entry = tk.Entry(self, width=40)
        self.payment_entry.grid(row=2, column=1, padx=10, pady=10)

        self.status_label = tk.Label(self, text="Status:")
        self.status_label.grid(row=3, column=0, padx=10, pady=10)
        self.status_entry = tk.Entry(self, width=40)
        self.status_entry.grid(row=3, column=1, padx=10, pady=10)

        # Botões
        self.save_button = tk.Button(self, text="Salvar", command=self.save_order)
        self.save_button.grid(row=4, column=0, padx=10, pady=10)
        self.back_button = tk.Button(self, text="Voltar", command=self.master.hide_order_form)
        self.back_button.grid(row=4, column=1, padx=10, pady=10)

        # Tabela para exibir os pedidos cadastrados
        self.order_table = ttk.Treeview(self, columns=("pedido_id", "cliente_id", "datetime", "payment", "status"), show="headings")
        self.order_table.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.order_table.heading("pedido_id", text="Pedido ID")
        self.order_table.heading("cliente_id", text="Cliente ID")
        self.order_table.heading("datetime", text="Data/Hora")
        self.order_table.heading("payment", text="Forma de Pagamento")
        self.order_table.heading("status", text="Status")

        # Carregar dados do banco de dados
        self.load_data()

    def save_order(self):
        # Verificar se os campos foram preenchidos
        if not self.client_id_entry.get() or not self.datetime_entry.get() or not self.payment_entry.get() or not self.status_entry.get():
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        # Criar um novo pedido com os dados inseridos
        order = {
            "cliente_id": self.client_id_entry.get(),
            "datetime": self.datetime_entry.get(),
            "payment": self.payment_entry.get(),
            "status": self.status_entry.get()
        }

        try:
            # Salvar o pedido no banco de dados
            cnx = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='pizzasnachtech'
            )
            cursor = cnx.cursor()
            cursor.execute("INSERT INTO pedidos (cliente_id, data_hora_pedido, forma_pagamento, status) VALUES (%s, %s, %s, %s)",
                           (order["cliente_id"], order["datetime"], order["payment"], order["status"]))
            cnx.commit()
            pedido_id = cursor.lastrowid
            cursor.close()
            cnx.close()

            # Adicionar o pedido à tabela
            self.order_table.insert("", "end", values=(pedido_id, order["cliente_id"], order["datetime"], order["payment"], order["status"]))

            # Limpar os campos de entrada
            self.client_id_entry.delete(0, tk.END)
            self.datetime_entry.delete(0, tk.END)
            self.payment_entry.delete(0, tk.END)
            self.status_entry.delete(0, tk.END)
        except mysql.connector.Error as err:
            messagebox.showerror("Erro de Banco de Dados", f"Erro: {err}")

    def load_data(self):
        try:
            # Conectar ao banco de dados
            cnx = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='pizzasnachtech'
            )
            cursor = cnx.cursor()
            cursor.execute("SELECT pedido_id, cliente_id, data_hora_pedido, forma_pagamento, status FROM pedidos")
            pedidos = cursor.fetchall()
            cursor.close()
            cnx.close()

            # Adicionar dados à tabela
            for pedido in pedidos:
                self.order_table.insert("", "end", values=pedido)
        except mysql.connector.Error as err:
            messagebox.showerror("Erro de Banco de Dados", f"Erro: {err}")

if __name__ == "__main__":
    app = PizzariaTech()
    app.mainloop()
