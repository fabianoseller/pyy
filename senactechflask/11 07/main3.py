import os
from flask import Flask, redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, validators
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from contextlib import contextmanager
import logging
from datetime import timedelta
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma-chave-secreta-padrao'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

csrf = CSRFProtect(app)

logging.basicConfig(filename='app.log', level=logging.ERROR)

@contextmanager
def get_db_connection():
    connection = None
    try:
        connection = conecta_no_banco_de_dados()
        yield connection
    finally:
        if connection and connection.is_connected():
            connection.close()

def conecta_no_banco_de_dados():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='pythonbas'
        )
        return conexao
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            criar_banco_de_dados()
            return conecta_no_banco_de_dados()
        else:
            logging.error(f"Erro de conexão com o banco de dados: {err}")
            raise

def criar_banco_de_dados():
    try:
        with mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        ) as conexao:
            cursor = conexao.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS pythonbas")
            cursor.execute("USE pythonbas")
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS contatos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL,
                    mensagem TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    email VARCHAR(255) NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_contatos (
                    usuario_id INT NOT NULL,
                    contato_id INT NOT NULL,
                    situacao VARCHAR(255) NOT NULL,
                    PRIMARY KEY (usuario_id, contato_id),
                    FOREIGN KEY (usuario_id) REFERENCES users(id) ON DELETE CASCADE,
                    FOREIGN KEY (contato_id) REFERENCES contatos(id) ON DELETE CASCADE
                )
            ''')
            conexao.commit()
    except mysql.connector.Error as err:
        logging.error(f"Erro ao criar o banco de dados ou tabelas: {err}")
        raise

class FormularioContato(FlaskForm):
    nome = StringField('Nome:', validators=[validators.DataRequired(), validators.Length(min=2, max=100)])
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()])
    mensagem = TextAreaField('Mensagem:', validators=[validators.DataRequired(), validators.Length(min=10, max=1000)])

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[validators.DataRequired(), validators.Length(min=4, max=20)])
    password = PasswordField('Password:', validators=[validators.DataRequired(), validators.Length(min=8)])

class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[validators.DataRequired(), validators.Length(min=4, max=20)])
    password = PasswordField('Password:', validators=[
        validators.DataRequired(),
        validators.Length(min=8),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()])

@app.before_request
def make_session_permanent():
    session.permanent = True

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        try:
            with get_db_connection() as conexao:
                cursor = conexao.cursor(dictionary=True)
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
            with get_db_connection() as conexao:
                cursor = conexao.cursor()
                cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
                if cursor.fetchone() is not None:
                    return render_template('register.html', form=form, msg='Esse usuário já existe')
                cursor.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s)',
                               (username, password, email))
                conexao.commit()
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
            with get_db_connection() as conexao:
                cursor = conexao.cursor()
                sql = "INSERT INTO contatos (nome, email, mensagem) VALUES (%s, %s, %s)"
                values = (nome, email, mensagem)
                cursor.execute(sql, values)
                conexao.commit()
            return redirect('/sucesso')
        except mysql.connector.Error as err:
            logging.error(f"Erro ao salvar dados no banco de dados: {err}")
            mensagem_erro = "Ocorreu um erro ao processar o seu contato. Tente novamente mais tarde."
            return render_template('erro.html', mensagem_erro=mensagem_erro), 500
    return render_template('contato.html', form=form)

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/consultar')
def consultar():
    if 'loggedin' in session:
        try:
            with get_db_connection() as conexao:
                cursor = conexao.cursor(dictionary=True)
                cursor.execute('SELECT * FROM contatos')
                contatos = cursor.fetchall()
            return render_template("consultar.html", contatos=contatos)
        except Exception as e:
            logging.error(f"Erro ao consultar contatos: {e}")
            return render_template('erro.html', mensagem_erro=str(e)), 500
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    criar_banco_de_dados()
    app.run(debug=False)