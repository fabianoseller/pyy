import mysql.connector
from mysql.connector import errorcode

def conecta_no_banco_de_dados():
    try:
        # Tenta se conectar ao banco de dados pythonbas
        conectacao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='pythonbas'
        )
        print('O banco de dados pythonbas existe e está pronto para uso.')
        return conectacao
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            # O banco de dados não existe, então cria-o
            criar_banco_de_dados()
            # Tenta se conectar novamente após criar o banco de dados
            conectacao = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='pythonbas'
            )
            return conectacao
        else:
            print("Erro de conexão com o banco de dados:", err)
            raise

def criar_banco_de_dados():
    try:
        # Conectar-se ao servidor MySQL
        conectacao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        )
        cursor = conectacao.cursor()
        
        # Criar o banco de dados
        cursor.execute('CREATE DATABASE IF NOT EXISTS pythonbas;')
        cursor.execute('USE pythonbas;')
        
        # Criar a tabela contatos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contatos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                mensagem TEXT NOT NULL
            );
        ''')

        # Criar a tabela usuarios
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            );
        ''')
        
        
        
            # Conectar-se ao banco de dados aula06 recém-criado
        cnx = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='pythonbas'  # Especificar o banco de dados
        )

    
        cursor = conectacao.cursor()
    
        cursor.execute('CREATE TABLE usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), email VARCHAR(255),senha VARCHAR(255));')
        
        

        conectacao.commit()
        print('Banco de dados e tabelas criados com sucesso!')
    except mysql.connector.Error as err:
        print("Erro ao criar o banco de dados ou tabelas:", err)
        raise
    finally:
        if conectacao.is_connected():
            cursor.close()
            conectacao.close()

# Testar a função de conexão
conexao = conecta_no_banco_de_dados()
