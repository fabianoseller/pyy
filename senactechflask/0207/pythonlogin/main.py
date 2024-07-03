from flask import Flask, redirect, render_template, request, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, validators
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma-chave-secreta'

# Função para conectar ao banco de dados
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
            conexao = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='pythonbas'
            )
            return conexao
        else:
            print("Erro de conexão com o banco de dados:", err)
            raise

def criar_banco_de_dados():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password=''
        )
        cursor = conexao.cursor()
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
        conexao.commit()
    except mysql.connector.Error as err:
        print("Erro ao criar o banco de dados ou tabelas:", err)
        raise
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()

class FormularioContato(FlaskForm):
    nome = StringField('Nome:', validators=[validators.DataRequired()])
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()])
    mensagem = TextAreaField('Mensagem:', validators=[validators.DataRequired(), validators.Length(min=10)])

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[validators.DataRequired()])
    password = PasswordField('Password:', validators=[validators.DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('Username:', validators=[validators.DataRequired()])
    password = PasswordField('Password:', validators=[validators.DataRequired()])
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()])

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data
        conexao = conecta_no_banco_de_dados()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account and check_password_hash(account[2], password):
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            return redirect(url_for('contato'))
        else:
            return render_template('login.html', form=form, msg='Usuário ou senha incorretos')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        email = form.email.data
        print(f"Tentando registrar usuário: {username}, {email}")
        try:
            conexao = conecta_no_banco_de_dados()
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            if cursor.fetchone() is not None:
                print(f"Usuário {username} já existe.")
                return render_template('register.html', form=form, msg='Esse usuário já existe')
            cursor.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s)', (username, password, email))
            conexao.commit()
            print(f"Usuário {username} registrado com sucesso.")
            return redirect(url_for('login'))
        except mysql.connector.Error as err:
            print(f"Erro ao registrar usuário: {err}")
            return render_template('register.html', form=form, msg='Erro ao registrar usuário')
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()
    return render_template('register.html', form=form)

@app.route('/', methods=['GET', 'POST'])
def contato():
    if 'loggedin' in session:
        form = FormularioContato()
        if form.validate_on_submit():
            nome = form.nome.data
            email = form.email.data
            mensagem = form.mensagem.data    
            try:
                conexao = conecta_no_banco_de_dados()
                cursor = conexao.cursor()
                sql = "INSERT INTO contatos (nome, email, mensagem) VALUES (%s, %s, %s)"
                values = (nome, email, mensagem)
                cursor.execute(sql, values)
                conexao.commit()
                print("Dados do formulário salvos com sucesso!")
            except mysql.connector.Error as err:
                print(f"Erro ao salvar dados no banco de dados: {err}")
                mensagem_erro = "Ocorreu um erro ao processar o seu contato. Tente novamente mais tarde."
                return render_template('erro.html', mensagem_erro=mensagem_erro), 500
            finally:
                if conexao.is_connected():
                    cursor.close()
                    conexao.close()
            return redirect('/sucesso')
        return render_template('contato.html', form=form)
    else:
        return redirect(url_for('login'))

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

@app.errorhandler(Exception)
def erro_geral(erro):
    mensagem_erro = str(erro)  
    return render_template('erro.html', mensagem_erro=mensagem_erro), 500

@app.route('/consultar')
def consultar():
    if 'loggedin' in session:
        try:
            conexao = conecta_no_banco_de_dados()
            cursor = conexao.cursor()
            cursor.execute('SELECT * FROM contatos')
            contatos = cursor.fetchall()
        except Exception as e:
            return render_template('erro.html', mensagem_erro=str(e)), 500
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()
        return render_template("consultar.html", contatos=contatos)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    criar_banco_de_dados()
    app.run(debug=True)
