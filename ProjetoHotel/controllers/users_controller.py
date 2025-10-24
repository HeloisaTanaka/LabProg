from flask import Blueprint, render_template, abort, request, session, redirect, url_for
from models.users import User, Users, addUser, validarEmail, verificarLogin, searchUserByEmail, searchUserById

user_bp = Blueprint('user_bp', __name__)
id = 1

@user_bp.route('/cadastro', methods=['POST'])
def cadastrar():
    global id
    nome = request.form.get('nome', '').strip()
    email = request.form.get('email', '').strip()
    senha = request.form.get('senha', '')
    confirmar_senha = request.form.get('verificador', '')
    perfil = request.form.get('perfil', '')

    campos = [nome, email, senha, confirmar_senha, perfil]
    for campo in campos:
        if not campo:
            return render_template('cadastro.html', erro='Todos os campos devem ser preenchidos')
    try:
        novoUser = User(str(id), nome, email, senha, confirmar_senha, str(perfil))
        id += 1
        addUser(novoUser)
        return redirect(url_for('login'))
    except:
        return render_template('cadastro.html', erro='Não foi possível cadastrar o usuário')


@user_bp.route('/login', methods=['POST'])
def logar():
    email = request.form.get('email', '')
    senha = request.form.get('senha', '')

    if not email or not senha:
        return render_template('login.html', erro='Preencha todos os campos')
    if not validarEmail(email):
        return render_template('login.html', erro='Email inválido')
        
    statusLogin = verificarLogin(email, senha)
    if statusLogin == True:
        user = searchUserByEmail(email)
        session['usuario_logado'] = user['id']
        session['perfil'] = user['perfil']
        return render_template('/')
    return render_template('/login.html', erro=statusLogin)
    
    


