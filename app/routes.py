from app import app
from flask import render_template,flash

from app.forms import FormsCadastro

@app.route('/')
def index():
    return  render_template('index.html', titulo = 'Home')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html',titulo = 'Sobre')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html',titulo = 'Projetos')

@app.route('/blog')
def blog():
    return render_template('blog.html',titulo = 'Blog')

@app.route('/cadastro', methods = ['GET', 'POST'])
def cadastro():
    cadastro = FormsCadastro()
    dicionario_cadastro = {}
    if cadastro.validate_on_submit():
        nome = cadastro.nome.data
        email = cadastro.email.data
        telefone = cadastro.telefone.data
        senha = cadastro.senha.data
        flash('Cadastro realizado com sucesso!')

        dicionario_cadastro = {
        'nome' : nome,
        'email' : email,
        'telefone' : telefone,
        'senha' : senha
    }
    
    return render_template('cadastro.html',titulo = 'Cadastro', cadastro=cadastro)


@app.route('/login')
def login():
    return render_template('login.html', titulo = 'Login')


