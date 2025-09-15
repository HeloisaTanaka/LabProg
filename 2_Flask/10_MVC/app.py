from flask import Flask, render_template, redirect, url_for, request, session
from models import UsuarioModel

app = Flask(__name__)
usuario_model = UsuarioModel()

@app.route('/usuarios')
def listar_usuarios():
    if not 'user' in session:
        return render_template('login.html')
    usuarios = usuario_model.get_todos()
    return render_template('usuarios.html', lista_de_usuarios = usuarios)

@app.route('/usuarios/novo', methods=['POST'])
def adicionar_usuarios():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    usuario_model.salvar(nome, email, senha)
    return redirect(url_for('listar_usuarios'))

@app.route('/login', methods=['POST'])
def logar():
    nome = request.form['nome']
    senha = request.form['senha']
    usuarios = usuario_model.get_todos()
    for user in usuarios:
        if user['nome'] == nome and user['senha'] == senha:
            return redirect(url_for('listar_usuarios'))
    else: 
        return render_template('login.html', mensagem = 'Usuário ou senha incorretos')



if __name__ == '__main__':
    app.run(debug=True)

    """Campo senha e excluir da lista, tela de login"""