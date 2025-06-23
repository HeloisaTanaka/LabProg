from flask import Flask, render_template, session, request, url_for, redirect

app = Flask(__name__)
app.secret_key = 'abcd'

@app.route('/logar', methods=['POST'])
def login():
    users = ['marcelinho', 'renata', 'alexandre']
    passwords = [123, 456, 789]
    username = request.form['username']
    password = request.form['password']
    
    #verficação de senha n funciona
    for i in range (len(users)):
        if username == users[i] and password == passwords[i]:
            session['username'] = username
            logado = True
            produtos = ["Maça", "Banana", "Laranja"]
            return render_template('home.html', produtos = produtos, username = username, logado = logado)

    logado = False
    return render_template('profile.html', user = username, logado = logado)

#@app.route('/')

#def carregar():
#    return render_template('login.html')

@app.route('/user/<username>')

def profile(username):
    return render_template('profile.html', user=username)

@app.route('/')
def carregarLogin():
    #produtos = ["Maça", "Banana", "Laranja"]
    #logado = True
    #return render_template("login.html", produtos=produtos, logado=logado)
    return render_template("login.html")

if __name__=='__main__':
    app.run(debug=True)