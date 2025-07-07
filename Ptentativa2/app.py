from flask import Flask, request, session, render_template, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = '123'

USUARIO_CADASTRADO = "Heloisa"
SENHA_CADASTRADA = "123"

@app.route('/', methods=['GET', 'POST'])
def index():
    user = request.cookies.get('username')
    if not user:
        return redirect(url_for('login'))
    
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    
    return render_template('index.html', user=user, counter=str(session['counter']))

#.@app.route('/logout')


if __name__ == '__main__':
    app.run(debug=True)
