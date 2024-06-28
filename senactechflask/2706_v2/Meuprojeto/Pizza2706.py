from flask import Flask, redirect, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators
from base_bd_config import conecta_no_banco_de_dados

app = Flask(__name__)
app.config['SECRET_KEY'] = 'uma-chave-secreta'

class FormularioContato(FlaskForm):
    nome = StringField('Nome:', validators=[validators.DataRequired()])
    email = StringField('Email:', validators=[validators.DataRequired(), validators.Email()])
    # assunto = StringField('Assunto:', validators=[validators.DataRequired()])
    mensagem = TextAreaField('Mensagem:', validators=[validators.DataRequired(), validators.Length(min=10)])

@app.route('/', methods=['GET', 'POST'])
def contato():
    form = FormularioContato()
    if form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data
        # assunto = form.assunto.data
        mensagem = form.mensagem.data    
        try:
            conectacao = conecta_no_banco_de_dados()
            cursor = conectacao.cursor()
           # sql = "INSERT INTO contatos (nome, email, assunto, mensagem) VALUES (%s, %s, %s, %s)"
            sql = "INSERT INTO contatos (nome, email, mensagem) VALUES (%s, %s, %s)"
            values = (nome, email, mensagem)
            cursor.execute(sql, values)
            conectacao.commit()
            print(f"Dados do formulário salvos com sucesso!")
        except conectacao.connector.Error as err:
            print(f"Erro ao salvar dados no banco de dados: {err}")
            mensagem_erro = "Ocorreu um erro ao processar o seu contato. Tente novamente mais tarde."
            return render_template('erro.html', mensagem_erro=mensagem_erro), 500
        finally:
            if conectacao is not None:
                conectacao.close()
        return redirect('/sucesso')
    else:
        return render_template('contato.html', form=form)

@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

@app.errorhandler(Exception)
def erro_geral(erro):
    mensagem_erro = str(erro)  
    return render_template('erro.html', mensagem_erro=mensagem_erro), 500

@app.route('/consultar')
def consultar():
    try:
        conectacao = conecta_no_banco_de_dados()
        cursor = conectacao.cursor()
        cursor.execute('SELECT * FROM contatos')
        contatos = cursor.fetchall()
    except Exception as e:
        return render_template('erro.html', mensagem_erro=str(e)), 500
    finally:
        if conectacao is not None:
            conectacao.close()
    return render_template("consultar.html", contatos=contatos)

if __name__ == '__main__':
    app.run(debug=True)
