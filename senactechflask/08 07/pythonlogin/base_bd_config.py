import mysql.connector
from mysql.connector import errorcode

def conecta_no_banco_de_dados():
    try:
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
            criar_banco_de_dados()
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
        conectacao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        )
        cursor = conectacao.cursor()
        
        cursor.execute('CREATE DATABASE IF NOT EXISTS pythonbas;')
        cursor.execute('USE pythonbas;')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contatos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                mensagem TEXT NOT NULL
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
            );
        ''')
        
        # Criar a tabela user_contatos com as relações especificadas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_contatos (
                usuario_id INT NOT NULL,
                contato_id INT NOT NULL,
                situacao VARCHAR(255) NOT NULL,
                PRIMARY KEY (usuario_id, contato_id),
                FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
                FOREIGN KEY (contato_id) REFERENCES contatos(id) ON DELETE CASCADE
            );
        ''')

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
if conexao.is_connected():
    print("Conexão estabelecida com sucesso!")
    conexao.close()
