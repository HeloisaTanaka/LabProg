from flask import Flask, render_template, request, flash, redirect, url_for, session, make_response, json

class usuario:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        
app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'
@app.route('/')
def index():
    return redirect(url_for('registrarUsuario'))

@app.route('/registrarUsuario', methods=['GET', 'POST'])
def registrarUsuario():
    if request.method == 'POST':
        user = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Validação simples do lado do servidor
        if not user or not email or not password:
            flash('Todos os campos são obrigatórios!', 'danger')
        else:
            flash(f'Usuário {user} cadastrado com sucesso!', 'success')
            #session['username'] = user
            #session['email'] = email
            #session['password'] = password
            #users = usuario(user, email, password)
            #with open('users.json', 'w') as file:
            #    json.dump(users, file)

            if 'dados' in session:
                session['dados'].append([user, email, password])
            else:
                session['dados'] = [[user, email, password]]

            cadastro = session['dados']
            return render_template('formulario.html', cadastro=cadastro)

            
        return redirect(url_for('registrarUsuario'))
        # flash(): Armazena uma mensagem que será exibida na próxima requisição. Isso
        # é útil para fornecer mensagens ao usuário.
    return render_template('formulario.html')
                           

if __name__ == '__main__':
    app.run(debug=True)

