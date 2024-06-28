import mysql.connector

def conecta_no_banco_de_dados():
    conectacao = mysql.connector.connect(host='127.0.0.1',user='root',password='')

    # Executar a instrução SQL para verificar se o banco de dados existe
    cursor = conectacao.cursor()
    cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "DB_aula27062024";')

    # Obter o número de resultados
    num_results = cursor.fetchone()[0]

    # Fechar a conexão com o banco de dados
    conectacao.close()

    # Se o número de resultados for maior que zero, o banco de dados existe
    if num_results > 0:
        print('O banco de dados DB_aula27062024 existe e esta pronto para uso.')
    else:
        # Conectar-se ao servidor MySQL para criar o banco de dados
        conectacao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        )

        # Criar o banco de dados DB_aula27062024
        cursor = conectacao.cursor()
        cursor.execute('CREATE DATABASE DB_aula27062024;')
        conectacao.commit()

    # Conectar-se ao banco de dados DB_aula27062024 recém-criado
        conectacao = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='DB_aula27062024'  # Especificar o banco de dados
        )

    
        cursor = conectacao.cursor()
        cursor.execute('CREATE TABLE contatos (id INT AUTO_INCREMENT PRIMARY KEY,nome VARCHAR(255) NOT NULL,email VARCHAR(255) NOT NULL,mensagem TEXT NOT NULL);')
         # Fechar a conexão com o banco de dados
        conectacao.commit()
        conectacao.close()
    try:
        conectacao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='DB_aula27062024'
        )
    except mysql.connector.Error as err:
        print("Erro de conexão com o banco de dados:", err)
        raise

    return conectacao