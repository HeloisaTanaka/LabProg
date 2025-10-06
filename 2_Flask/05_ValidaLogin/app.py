from flask import Flask, render_template, session, request, url_for, redirect

app = Flask(__name__)
app.secret_key = 'abcd'

@app.route('/')
def carregarLogin():
    return render_template("login.html")

@app.route('/logar', methods=['POST'])
def login():
    users = ['marcelinho', 'renata', 'alexandre']
    passwords = ['123', '456', '789']
    username = request.form['username']
    password = request.form['password']
    index = 0
    for i in users:
        if username == i and password == passwords[index]:
            session['username'] = username 
            logado = True
            produtos = ["Maçã", "Banana", "Laranja"]
            return render_template('home.html', produtos = produtos, username = username, logado = logado)
        index += 1
    logado = False
    return render_template('login.html', message='Usuário ou senha incorretos')

@app.route('/user/<username>')
def profile(username):
    return render_template('profile.html', user=username)

if __name__=='__main__':
    app.run(debug=True)