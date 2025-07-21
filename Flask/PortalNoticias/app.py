#Atividade para melhor compreensão da manipulação de cookies e sessões.
# Session para armazenar o número de visitas à página, numa mesma sessão
# Cookies para salvar e armazenar a preferência de tema e notícias do usuário

from flask import Flask, request, session, render_template, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = '123'

USUARIO_CADASTRADO = "Heloisa"
SENHA_CADASTRADA = "123"

@app.route('/', methods=['GET', 'POST'])
def login():
    mensagem = ''

    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        if USUARIO_CADASTRADO == user and SENHA_CADASTRADA == password:
            resposta = make_response(redirect(url_for('home')))
            resposta.set_cookie('username', user, max_age=60*30)
            return resposta
        else:
            mensagem = 'Usuário ou senha inválidos'
    return render_template('login.html', error = mensagem)

@app.route('/home')
def home():
    user = request.cookies.get('username')
    if not user:
        return redirect(url_for("login"))
    
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1

    tema = request.cookies.get('tema')
    if not tema:
        tema = 'claro'

    page = request.cookies.get('last_page')

    if not page:
        return render_template('home.html', user=user, counter=str(session['counter']), tema=tema)
    else:
        return render_template('home.html', user=user, counter=str(session['counter']), tema=tema, page = page)
    
    
@app.route('/atualizar_conteudo')
def conteudo():
    user = request.cookies.get('username')
    page = request.cookies.get('last_page')
    tema = request.cookies.get('tema')
    return render_template('home.html', page=page, tema=tema, user=user, counter = session['counter'])

@app.route('/page', methods=['POST'])
def page():
    if request.method == 'POST':
        if request.form["page"] == 'esportes':
            response = make_response(redirect(url_for('conteudo')))
            response.set_cookie('last_page', 'esportes', max_age=60*30)
        elif request.form['page'] == 'entretenimento':
            response = make_response(redirect(url_for('conteudo')))
            response.set_cookie('last_page', 'entretenimento', max_age=60*30)
        elif request.form['page'] == 'lazer':
            response = make_response(redirect(url_for('conteudo')))
            response.set_cookie('last_page', 'lazer', max_age=60*30)
        else:
            return render_template('home.html', page='erro')
        
        return response

@app.route('/tema', methods=['POST'])
def tema():
    if request.method == 'POST':
        if request.form['tema'] == 'claro':
            response = redirect(url_for('conteudo'))
            response.set_cookie('tema', 'claro', max_age=60*30)
        elif request.form['tema'] == 'escuro':
            response = redirect(url_for('conteudo'))
            response.set_cookie('tema', 'escuro', max_age=60*30)
        return response
        
@app.route('/logout', methods=['POST'])
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('username', '', expires=0)
    response.set_cookie('tema', '', expires=0)
    response.set_cookie('last_page', '', expires=0)
    session['counter'] = 0
    return response

if __name__ == '__main__':
    app.run(debug=True)
