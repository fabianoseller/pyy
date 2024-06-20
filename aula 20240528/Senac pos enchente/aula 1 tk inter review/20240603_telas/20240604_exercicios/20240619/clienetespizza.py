import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class ClientForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Clientes")
        self.master.geometry("500x400")

        # Criar labels e entrys para os campos de entrada
        self.email_label = tk.Label(master, text="E-mail:")
        self.email_label.pack()
        self.email_entry = tk.Entry(master, width=40)
        self.email_entry.pack()

        self.cliente_id_label = tk.Label(master, text="ID do Cliente:")
        self.cliente_id_label.pack()
        self.cliente_id_entry = tk.Entry(master, width=40)
        self.cliente_id_entry.pack()

        self.nome_label = tk.Label(master, text="Nome:")
        self.nome_label.pack()
        self.nome_entry = tk.Entry(master, width=40)
        self.nome_entry.pack()

        self.endereco_label = tk.Label(master, text="Endereço:")
        self.endereco_label.pack()
        self.endereco_entry = tk.Entry(master, width=40)
        self.endereco_entry.pack()

        self.telefone_label = tk.Label(master, text="Telefone:")
        self.telefone_label.pack()
        self.telefone_entry = tk.Entry(master, width=40)
        self.telefone_entry.pack()

        # Botão para salvar o cliente
        self.save_button = tk.Button(master, text="Salvar", command=self.save_client)
        self.save_button.pack()

        # Tabela para exibir os clientes cadastrados
        self.client_table = ttk.Treeview(master, columns=("email", "cliente_id", "nome", "endereco", "telefone"), show="headings")
        self.client_table.pack(fill="both", expand=True)
        self.client_table.heading("email", text="E-mail")
        self.client_table.heading("cliente_id", text="ID do Cliente")
        self.client_table.heading("nome", text="Nome")
        self.client_table.heading("endereco", text="Endereço")
        self.client_table.heading("telefone", text="Telefone")

    def save_client(self):
        # Verificar se os campos foram preenchidos
        if not self.email_entry.get() or not self.cliente_id_entry.get() or not self.nome_entry.get() or not self.endereco_entry.get() or not self.telefone_entry.get():
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        # Criar um novo cliente com os dados inseridos
        client = {
            "email": self.email_entry.get(),
            "cliente_id": self.cliente_id_entry.get(),
            "nome": self.nome_entry.get(),
            "endereco": self.endereco_entry.get(),
            "telefone": self.telefone_entry.get()
        }

        # Salvar o cliente no banco de dados
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='pizzasnachtech'
        )
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO clientes (email, cliente_id, nome, endereco, telefone) VALUES (%s, %s, %s, %s, %s)", (client["email"], client["cliente_id"], client["nome"], client["endereco"], client["telefone"]))
        cnx.commit()
        cursor.close()
        cnx.close()

        # Adicionar o cliente à tabela
        self.client_table.insert("", "end", values=(client["email"], client["cliente_id"], client["nome"], client["endereco"], client["telefone"]))

        # Limpar os campos de entrada
        self.email_entry.delete(0, tk.END)
        self.cliente_id_entry.delete(0, tk.END)
        self.nome_entry.delete(0, tk.END)
        self.endereco_entry.delete(0, tk.END)
        self.telefone_entry.delete(0, tk.END)

root = tk.Tk()
client_form = ClientForm(root)
root.mainloop()
