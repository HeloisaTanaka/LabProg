from flask import Flask, render_template, request, redirect, url_for, make_response, session

#Fazer o contador de página
#Fazer as preferência de tema
#Fazer a última página acessada



app = Flask(__name__)
app.secret_key = '123'

USUARIO_CADASTRADO = "Heloisa"
SENHA_CADASTRADA = "123"

@app.route('/', methods=['GET', 'POST'])
def login():
    mensagem = ""

    if request.method == "POST":
        usuario = request.form['username']
        senha = request.form['password']
        if usuario == USUARIO_CADASTRADO and senha == SENHA_CADASTRADA:
            resposta = make_response(redirect(url_for('bemvindo')))
            resposta.set_cookie('username', usuario, max_age=60*30)

            return resposta

        else:
            mensagem = "Usuário ou senha inválidos. Tente novamente."

    return render_template('login.html', error=mensagem)

@app.route('/bemvindo')
#def ultimaPag():
    #last_page = request.cookies.get('ultimaPag')
    #return render_template('bemvindo.html', ultimaPag=last_page)


def bemvindo():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1

    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    
    resposta = make_response(render_template('bemvindo.html', user=username))
    resposta.set_cookie('counter', str(session['counter']), max_age=60*30)
    return resposta

@app.route('/esportes')
def esportes():
    pagina = 'esportes'
    user = request.cookies.get('username')
    resposta = make_response(render_template('esportes'))
    resposta.set_cookie('ultimaPag', pagina, max_age=60*30)
    return render_template('esportes.html', user = user)


@app.route('/entretenimento')
def entretenimento():
    pagina = 'entretenimento'
    resposta = make_response(redirect(url_for('esportes')))
    resposta.set_cookie('ultimaPag', pagina, max_age=60*30)
    user = request.cookies.get('username')
    render_template('entretenimento.html', user = user)

@app.route('/lazer')
def lazer():
    user = request.cookies.get('username')
    if not user:
        return redirect(url_for('login'))
    
    resposta = make_response(render_template('lazer.html', user=user))
    resposta.set_cookie('ultimaPag', 'lazer', max_age=60*30)
    return resposta

@app.route('/logout')
def logout():
    resposta = make_response(redirect(url_for('login')))

    resposta.set_cookie('username', '', expires=0)
    return resposta

if __name__ == '__main__':
    app.run(debug=True)