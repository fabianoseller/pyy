import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class OrderForm:
    def __init__(self, master):
        self.master = master
        self.master.title("Cadastro de Pedidos")
        self.master.geometry("600x500")

        # Criar labels e entrys para os campos de entrada
        self.datetime_label = tk.Label(master, text="Data/Hora do Pedido:")
        self.datetime_label.pack()
        self.datetime_entry = tk.Entry(master, width=40)
        self.datetime_entry.pack()

        self.payment_label = tk.Label(master, text="Forma de Pagamento:")
        self.payment_label.pack()
        self.payment_entry = tk.Entry(master, width=40)
        self.payment_entry.pack()

        self.status_label = tk.Label(master, text="Status:")
        self.status_label.pack()
        self.status_entry = tk.Entry(master, width=40)
        self.status_entry.pack()

        # Botão para salvar o pedido
        self.save_button = tk.Button(master, text="Salvar", command=self.save_order)
        self.save_button.pack()

        # Tabela para exibir os pedidos cadastrados
        self.order_table = ttk.Treeview(master, columns=("datetime", "payment", "status"), show="headings")
        self.order_table.pack(fill="both", expand=True)
        self.order_table.heading("datetime", text="Data/Hora")
        self.order_table.heading("payment", text="Forma de Pagamento")
        self.order_table.heading("status", text="Status")

    def save_order(self):
        # Verificar se os campos foram preenchidos
        if not self.datetime_entry.get() or not self.payment_entry.get() or not self.status_entry.get():
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        # Criar um novo pedido com os dados inseridos
        order = {
            "datetime": self.datetime_entry.get(),
            "payment": self.payment_entry.get(),
            "status": self.status_entry.get()
        }

        # Salvar o pedido no banco de dados
        cnx = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='pizzasnachtech'
        )
        cursor = cnx.cursor()
        cursor.execute("INSERT INTO pedidos (data_hora_pedido, forma_pagamento, status) VALUES (%s, %s, %s)", (order["datetime"], order["payment"], order["status"]))
        cnx.commit()
        cursor.close()
        cnx.close()

        # Adicionar o pedido à tabela
        self.order_table.insert("", "end", values=(order["datetime"], order["payment"], order["status"]))

        # Limpar os campos de entrada
        self.datetime_entry.delete(0, tk.END)
        self.payment_entry.delete(0, tk.END)
        self.status_entry.delete(0, tk.END)

root = tk.Tk()
order_form = OrderForm(root)
root.mainloop()