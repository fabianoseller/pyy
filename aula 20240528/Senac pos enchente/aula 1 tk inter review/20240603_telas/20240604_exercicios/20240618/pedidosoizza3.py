# Conectar-se ao banco de dados
import mysql.connector
# Conectar-se ao banco de dados
cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='pizzasnachtech'
)

# Criar um cursor
cursor = cnx.cursor()

# Inserir pedidos
cursor.execute("""
    INSERT INTO pedidos (pedido_id, cliente_id, data_hora_pedido, forma_pagamento, status)
    VALUES
        (14, 14, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
        (15, 15, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
        (16, 16, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
        (17, 17, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
        (18, 18, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
        (19, 19, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
        (20, 20, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
        (21, 21, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
        (22, 22, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
        (23, 23, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente'),
        (24, 24, '2024-06-19 15:59:00', 'Cartão de Crédito', 'Pendente')
""")

# Confirmar as alterações
cnx.commit()

# Consultar a tabela pedidos
print("Dados da tabela pedidos:")
cursor.execute("SELECT * FROM pedidos")
for row in cursor:
    print(f"Pedido ID: {row[0]}, Cliente ID: {row[1]}, Data/Hora: {row[2]}, Forma de Pagamento: {row[3]}, Status: {row[4]}")

# Fechar a conexão
cnx.close()
