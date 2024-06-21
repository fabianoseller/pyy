class OrderForm:
    def __init__(self):
        self.orders = []
        self.customers = []

    ## Funcionalidades de Clientes
    def load_customers(self):
        try:
            with open("customers.txt", "r") as file:
                for line in file:
                    customer = line.strip().split(",")
                    self.customers.append({
                        "id": int(customer[0]),
                        "name": customer[1],
                        "email": customer[2],
                        "phone": customer[3],
                    })
        except FileNotFoundError:
            print("Nenhum cliente encontrado.")

    def save_customers(self):
        with open("customers.txt", "w") as file:
            for customer in self.customers:
                file.write(f"{customer['id']},{customer['name']},{customer['email']},{customer['phone']}\n")

    def add_customer(self, name, email, phone):
        new_customer = {
            "id": len(self.customers) + 1,
            "name": name,
            "email": email,
            "phone": phone,
        }
        self.customers.append(new_customer)
        print(f"Cliente adicionado com sucesso: {new_customer['id']}")

    def update_customer(self, customer_id, name, email, phone):
        for customer in self.customers:
            if customer["id"] == customer_id:
                customer["name"] = name
                customer["email"] = email
                customer["phone"] = phone
                print(f"Cliente atualizado com sucesso: {customer_id}")
                return
        print(f"Cliente não encontrado: {customer_id}")

    def delete_customer(self, customer_id):
        for customer in self.customers:
            if customer["id"] == customer_id:
                self.customers.remove(customer)
                print(f"Cliente deletado com sucesso: {customer_id}")
                return
        print(f"Cliente não encontrado: {customer_id}")

    ## Funcionalidades de Pedidos
    def load_orders(self):
        try:
            with open("orders.txt", "r") as file:
                for line in file:
                    order = line.strip().split(",")
                    self.orders.append({
                        "id": int(order[0]),
                        "customer_id": int(order[1]),
                        "order_date": order[2],
                        "total": float(order[3]),
                    })
        except FileNotFoundError:
            print("Nenhum pedido encontrado.")

    def save_orders(self):
        with open("orders.txt", "w") as file:
            for order in self.orders:
                file.write(f"{order['id']},{order['customer_id']},{order['order_date']},{order['total']}\n")

    def add_order(self, customer_id, order_date, total):
        new_order = {
            "id": len(self.orders) + 1,
            "customer_id": customer_id,
            "order_date": order_date,
            "total": total,
        }
        self.orders.append(new_order)
        print(f"Pedido adicionado com sucesso: {new_order['id']}")

    def update_order(self, order_id, customer_id, order_date, total):
        for order in self.orders:
            if order["id"] == order_id:
                order["customer_id"] = customer_id
                order["order_date"] = order_date
                order["total"] = total
                print(f"Pedido atualizado com sucesso: {order_id}")
                return
        print(f"Pedido não encontrado: {order_id}")

    def delete_order(self, order_id):
        for order in self.orders:
            if order["id"] == order_id:
                self.orders.remove(order)
                print(f"Pedido deletado com sucesso: {order_id}")
                return
        print(f"Pedido não encontrado: {order_id}")

    def display_customers(self):
        for customer in self.customers:
            print(f"Cliente {customer['id']}:")
            print(f"  Nome: {customer['name']}")
            print(f"  Email: {customer['email']}")
            print(f"  Telefone: {customer['phone']}")

    def display_orders(self):
        for order in self.orders:
            print(f"Pedido {order['id']}:")
            print(f"  ID do Cliente: {order['customer_id']}")
            print(f"  Data do pedido: {order['order_date']}")
            print(f"  Total: {order['total']}")

def main_menu():
    order_form = OrderForm()
    while True:
        print("\nMenu Principal:")
        print("1. Gerenciar Clientes")
        print("2. Gerenciar Pedidos")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            customer_menu(order_form)
        elif choice == "2":
            order_menu(order_form)
        elif choice == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def customer_menu(order_form):
    while True:
        print("\nMenu de Clientes:")
        print("1. Carregar Clientes")
        print("2. Adicionar Cliente")
        print("3. Atualizar Cliente")
        print("4. Deletar Cliente")
        print("5. Exibir Clientes")
        print("6. Voltar")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            order_form.load_customers()
        elif choice == "2":
            name = input("Nome do cliente: ")
            email = input("Email do cliente: ")
            phone = input("Telefone do cliente: ")
            order_form.add_customer(name, email, phone)
        elif choice == "3":
            customer_id = int(input("ID do cliente: "))
            name = input("Novo nome do cliente: ")
            email = input("Novo email do cliente: ")
            phone = input("Novo telefone do cliente: ")
            order_form.update_customer(customer_id, name, email, phone)
        elif choice == "4":
            customer_id = int(input("ID do cliente: "))
            order_form.delete_customer(customer_id)
        elif choice == "5":
            order_form.display_customers()
        elif choice == "6":
            return
        else:
            print("Opção inválida. Tente novamente.")

def order_menu(order_form):
    while True:
        print("\nMenu de Pedidos:")
        print("1. Carregar Pedidos")
        print("2. Adicionar Pedido")
        print("3. Atualizar Pedido")
        print("4. Deletar Pedido")
        print("5. Exibir Pedidos")
        print("6. Voltar")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            order_form.load_orders()
        elif choice == "2":
            customer_id = int(input("ID do cliente: "))
            order_date = input("Data do pedido (YYYY-MM-DD): ")
            total = float(input("Total do pedido: "))
            order_form.add_order(customer_id, order_date, total)
        elif choice == "3":
            order_id = int(input("ID do pedido: "))
            customer_id = int(input("Novo ID do cliente: "))
            order_date = input("Nova data do pedido (YYYY-MM-DD): ")
            total = float(input("Novo total do pedido: "))
            order_form.update_order(order_id, customer_id, order_date, total)
        elif choice == "4":
            order_id = int(input("ID do pedido: "))
            order_form.delete_order(order_id)
        elif choice == "5":
            order_form.display_orders()
        elif choice == "6":
            return
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main_menu()