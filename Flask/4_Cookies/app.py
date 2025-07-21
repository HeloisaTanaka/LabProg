from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

USUARIO_CADASTRADO = "Heloisa"
SENHA_CADASTRADA = "123"

@app.route('/', methods=['GET', 'POST'])
def login():
    mensagem = ""

    if request.method == "POST":
        usuario = request.form['username'] #Assume o valor do input cujo name='username', no form HTML
        senha = request.form['password']
        if usuario == USUARIO_CADASTRADO and senha == SENHA_CADASTRADA:
            resposta = make_response(redirect(url_for('bemvindo'))) #Quando resposta for retornada, executará a rota /bemvindo
            resposta.set_cookie('username', usuario, max_age=60*10) 
            #Cria um cookie que armazena o valor de usuario numa variável própria chamada username
            #max_age=tempo, especifica a duração do cookie, nesse caso 60s*10 = 10 min
            return resposta #Ao retornar a resposta, o redirect(url_for('bemvindo)) será executado

        else:
            mensagem = "Usuário ou senha inválidos. Tente novamente."

    return render_template('login.html', error=mensagem)

@app.route('/bemvindo')
def bemvindo():
    username = request.cookies.get('username') #Pega o valor armazenado na variável 'username' do cookie
    if not username:
        return redirect(url_for('login'))
    
    return render_template('bemvindo.html', user=username)


@app.route('/logout')
def logout():
    resposta = make_response(redirect(url_for('login')))

    resposta.set_cookie('username', '', expires=0) #Apaga o valor de 'username' do cookie
    return resposta

if __name__ == '__main__':
    app.run(debug=True)