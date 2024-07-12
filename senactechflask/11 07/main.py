from flask import Flask, redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, validators
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import logging
from contextlib import contextmanager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma-chave-secreta'

logging.basicConfig(filename='app.log', level=logging.ERROR)

@contextmanager
def get_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='pythonbas'
        )
        yield connection
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            criar_banco_de_dados()
            connection = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='pythonbas'
            )
            yield connection
        else:
            logging.error(f"Erro de conexão com o banco de dados: {err}")
            raise
    finally:
        if connection and connection.is_connected():
            connection.close()

def criar_banco_de_dados():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        )
        cursor = connection.cursor()
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
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_contatos (
                users_id INT NOT NULL,
                contatos_id INT NOT NULL,
                situacao VARCHAR(255) NOT NULL,
                PRIMARY KEY (contatos_id, users_id),
                FOREIGN KEY (users_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (contatos_id) REFERENCES contatos(id) ON DELETE CASCADE
            );
        ''')
        connection.commit()
    except mysql.connector.Error as err:
        logging.error(f"Erro ao criar o banco de dados ou tabelas: {err}")
        raise
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

class FormularioContato(FlaskForm):
    nome = StringField('Nome:', validators=[validators.DataRequired()])
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()])
    mensagem = TextAreaField('Mensagem:', validators=[validators.DataRequired(), validators.Length(min=10)])

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[validators.DataRequired()])
    password = PasswordField('Password:', validators=[validators.DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[validators.DataRequired(), validators.Length(min=4, max=20)])
    password = PasswordField('Password:', validators=[
        validators.DataRequired(),
        validators.Length(min=8),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password', validators=[validators.DataRequired()])
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()])

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        try:
            with get_db_connection() as connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
                account = cursor.fetchone()
                if account and check_password_hash(account['password'], password):
                    session['loggedin'] = True
                    session['id'] = account['id']
                    session['username'] = account['username']
                    return redirect(url_for('contato'))
                else:
                    return render_template('login.html', form=form, msg='Usuário ou senha incorretos')
        except mysql.connector.Error as err:
            logging.error(f"Erro ao fazer login: {err}")
            return render_template('erro.html', mensagem_erro="Erro ao processar o login"), 500
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        email = form.email.data
        try:
            with get_db_connection() as connection:
                cursor = connection.cursor()
                cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
                if cursor.fetchone() is not None:
                    return render_template('register.html', form=form, msg='Esse usuário já existe')
                cursor.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s)', 
                               (username, password, email))
                connection.commit()
            return redirect(url_for('login'))
        except mysql.connector.Error as err:
            logging.error(f"Erro ao registrar usuário: {err}")
            return render_template('register.html', form=form, msg='Erro ao registrar usuário')
    return render_template('register.html', form=form)

@app.route('/', methods=['GET', 'POST'])
def contato():
    form = FormularioContato()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        mensagem = form.mensagem.data
        try:
            with get_db_connection() as connection:
                cursor = connection.cursor()
                sql = "INSERT INTO contatos (nome, email, mensagem) VALUES (%s, %s, %s)"
                values = (nome, email, mensagem)
                cursor.execute(sql, values)
                connection.commit()
            return redirect('/sucesso')
        except mysql.connector.Error as err:
            logging.error(f"Erro ao salvar dados no banco de dados: {err}")
            mensagem_erro = "Ocorreu um erro ao processar o seu contato. Tente novamente mais tarde."
            return render_template('erro.html', mensagem_erro=mensagem_erro), 500
    return render_template('contato.html', form=form)

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

@app.route('/consultar')
def consultar():
    if 'loggedin' in session:
        try:
            with get_db_connection() as connection:
                cursor = connection.cursor(dictionary=True)
                
                # Consulta usuários
                cursor.execute('SELECT users_id, username, email FROM users')
                users = cursor.fetchall()
                
                # Consulta contatos
                cursor.execute('SELECT contatos_id, nome, email, mensagem FROM contatos')
                contatos = cursor.fetchall()
                
                # Consulta relação user_contatos
                cursor.execute('''
                    SELECT uc.users_id, u.username, 
                           uc.contatos_id, c.nome, uc.situacao
                    FROM user_contatos uc
                    JOIN users u ON uc.users_id = u.users_id
                    JOIN contatos c ON uc.contatos_id = c.contatos_id
                ''')
                user_contatos = cursor.fetchall()
                
            return render_template("consultar.html", users=users, contatos=contatos, user_contatos=user_contatos)
        except Exception as e:
            logging.error(f"Erro ao consultar dados: {e}")
            return render_template('erro.html', mensagem_erro=str(e)), 500
    else:
        return redirect(url_for('login'))
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
      form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        try:
            with get_db_connection() as connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
                user = cursor.fetchone()
                if user and check_password_hash(user['password'], password):
                    session['loggedin'] = True
                    session['id'] = user['id']
                    session['username'] = user['username']
                    return redirect(url_for('dashboard'))
                else:
                    return render_template('login.html', form=form, msg='Usuário ou senha incorretos')
        except mysql.connector.Error as err:
            logging.error(f"Erro ao fazer login: {err}")
            return render_template('erro.html', mensagem_erro="Erro ao processar o login"), 500
    return render_template('login.html', form=form)
    
    
    @app.route('/dashboard')
    def dashboard():
     if 'loggedin' in session:
        try:
            with get_db_connection() as connection:
                cursor = connection.cursor(dictionary=True)
                cursor.execute('SELECT * FROM contatos WHERE email = (SELECT email FROM users WHERE id = %s)', (session['id'],))
                messages = cursor.fetchall()
            return render_template('dashboard.html', username=session['username'], messages=messages)
        except mysql.connector.Error as err:
            logging.error(f"Erro ao buscar mensagens: {err}")
            return render_template('erro.html', mensagem_erro="Erro ao buscar mensagens"), 500
    return redirect(url_for('login'))
    
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.errorhandler(Exception)
def erro_geral(erro):
    logging.error(f"Erro não tratado: {str(erro)}")
    return render_template('erro.html', mensagem_erro="Ocorreu um erro inesperado."), 500

if __name__ == '__main__':
    criar_banco_de_dados()
    app.run(debug=True)