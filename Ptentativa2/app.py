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
            #session['username'] = user
        else:
            mensagem = 'Usuário ou senha inválidos'
    return render_template('login.html', mensagem = mensagem)

@app.route('/home')
def home():
    user = request.cookies.get('username')
    if not user:
        return redirect(url_for("login"))
    
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1

    last_page = request.cookies.get('last_page')
    if not last_page:
        return render_template('home.html', user=user, counter=str(session['counter']))
    else:
        return render_template('home.html', user=user, counter=str(session['counter']), last_page = last_page)

@app.route('/page', methods=['POST'])
def page():
    user = request.cookies.get('username')
    if request.method == 'POST':
        if request.form["page"] == 'esportes':
            response = make_response(render_template('home.html', page='esportes', user = user, counter=str(session['counter'])))
            response.set_cookie('last_page', 'esportes', max_age=60*30)
        elif request.form['page'] == 'entretenimento':
            response = make_response(render_template('home.html', page='entretenimento', user = user, counter=str(session['counter'])))
            response.set_cookie('last_page', 'entretenimento', max_age=60*30)
        elif request.form['page'] == 'lazer':
            response = make_response(render_template('home.html', page='lazer', user = user, counter=str(session['counter'])))
            response.set_cookie('last_page', 'lazer', max_age=60*30)
        else:
            return render_template('home.html', page='erro')
        return response



if __name__ == '__main__':
    app.run(debug=True)
