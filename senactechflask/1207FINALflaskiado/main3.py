# https://codepen.io/GrandvincentMarion/pen/epEPjp
from flask import Flask, redirect, render_template, request, session, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, validators, SelectField
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

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
            return conecta_no_banco_de_dados()
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
                contatos_id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                mensagem TEXT NOT NULL,
                status ENUM('Pendente', 'Em Atendimento', 'Resolvido') DEFAULT 'Pendente'
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                users_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL UNIQUE,
                role ENUM('admin', 'user') DEFAULT 'user'
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_contatos (
                users_id INT NOT NULL,
                contatos_id INT NOT NULL,
                data_atribuicao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (contatos_id, users_id),
                FOREIGN KEY (users_id) REFERENCES users(users_id) ON DELETE CASCADE,
                FOREIGN KEY (contatos_id) REFERENCES contatos(contatos_id) ON DELETE CASCADE
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

class AtribuirContatoForm(FlaskForm):
    usuario = SelectField('Atribuir para:', coerce=int)

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'loggedin' not in session:
            flash('Por favor, faça login para acessar esta página.', 'warning')
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        conexao = conecta_no_banco_de_dados()
        cursor = conexao.cursor(dictionary=True)
        try:
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            account = cursor.fetchone()
            if account and check_password_hash(account['password'], password):
                session['loggedin'] = True
                session['id'] = account['users_id']
                session['username'] = account['username']
                session['role'] = account['role']
                flash('Login realizado com sucesso!', 'success')
                return redirect(url_for('contato'))
            else:
                flash('Usuário ou senha incorretos', 'danger')
        finally:
            cursor.close()
            conexao.close()
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        email = form.email.data
        try:
            conexao = conecta_no_banco_de_dados()
            cursor = conexao.cursor()
            cursor.execute('INSERT INTO users (username, password, email) VALUES (%s, %s, %s)', (username, password, email))
            conexao.commit()
            flash('Registro realizado com sucesso! Faça login para continuar.', 'success')
            return redirect(url_for('login'))
        except mysql.connector.Error as err:
            flash(f'Erro ao registrar usuário: {err}', 'danger')
        finally:
            cursor.close()
            conexao.close()
    return render_template('register.html', form=form)

@app.route('/', methods=['GET', 'POST'])
def contato():
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
            flash('Mensagem enviada com sucesso!', 'success')
            return redirect(url_for('sucesso'))
        except mysql.connector.Error as err:
            flash(f'Erro ao enviar mensagem: {err}', 'danger')
            return redirect(url_for('contato'))
        finally:
            cursor.close()
            conexao.close()
    return render_template('contato.html', form=form)

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

@app.errorhandler(Exception)
def erro_geral(erro):
    mensagem_erro = str(erro)  
    return render_template('erro.html', mensagem_erro=mensagem_erro), 500

@app.route('/consultar')
@login_required
def consultar():
    try:
        conexao = conecta_no_banco_de_dados()
        cursor = conexao.cursor(dictionary=True)
        if session['role'] == 'admin':
            cursor.execute('''
                SELECT c.*, u.username as atribuido_para
                FROM contatos c
                LEFT JOIN user_contatos uc ON c.contatos_id = uc.contatos_id
                LEFT JOIN users u ON uc.users_id = u.users_id
            ''')
        else:
            cursor.execute('''
                SELECT c.*, u.username as atribuido_para
                FROM contatos c
                LEFT JOIN user_contatos uc ON c.contatos_id = uc.contatos_id
                LEFT JOIN users u ON uc.users_id = u.users_id
                WHERE uc.users_id = %s OR uc.users_id IS NULL
            ''', (session['id'],))
        contatos = cursor.fetchall()
        return render_template("consultar.html", contatos=contatos)
    except Exception as e:
        flash(f'Erro ao consultar contatos: {e}', 'danger')
        return redirect(url_for('contato'))
    finally:
        cursor.close()
        conexao.close()

@app.route('/atribuir/<int:contato_id>', methods=['GET', 'POST'])
@login_required
def atribuir_contato(contato_id):
    if session['role'] != 'admin':
        flash('Você não tem permissão para atribuir contatos.', 'danger')
        return redirect(url_for('consultar'))

    form = AtribuirContatoForm()
    
    conexao = conecta_no_banco_de_dados()
    cursor = conexao.cursor(dictionary=True)
    
    try:
        cursor.execute('SELECT users_id, username FROM users WHERE role = "user"')
        usuarios = cursor.fetchall()
        form.usuario.choices = [(u['users_id'], u['username']) for u in usuarios]

        if form.validate_on_submit():
            usuario_id = form.usuario.data
            cursor.execute('INSERT INTO user_contatos (users_id, contatos_id) VALUES (%s, %s) ON DUPLICATE KEY UPDATE users_id = %s', 
                           (usuario_id, contato_id, usuario_id))
            conexao.commit()
            flash('Contato atribuído com sucesso!', 'success')
            return redirect(url_for('consultar'))

        return render_template('atribuir_contato.html', form=form, contato_id=contato_id)
    except Exception as e:
        flash(f'Erro ao atribuir contato: {e}', 'danger')
        return redirect(url_for('consultar'))
    finally:
        cursor.close()
        conexao.close()

@app.route('/atualizar_status/<int:contato_id>', methods=['POST'])
@login_required
def atualizar_status(contato_id):
    novo_status = request.form.get('status')
    if novo_status not in ['Pendente', 'Em Atendimento', 'Resolvido']:
        flash('Status inválido.', 'danger')
        return redirect(url_for('consultar'))

    try:
        conexao = conecta_no_banco_de_dados()
        cursor = conexao.cursor()
        cursor.execute('UPDATE contatos SET status = %s WHERE contatos_id = %s', (novo_status, contato_id))
        conexao.commit()
        flash('Status atualizado com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao atualizar status: {e}', 'danger')
    finally:
        cursor.close()
        conexao.close()
    return redirect(url_for('consultar'))

@app.route('/logout')
def logout():
    session.clear()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    criar_banco_de_dados()
    app.run(debug=True)