# Verificação do lado do servidor

#OBS.: as condições de verificação dos campos no JS e no python estão diferentes, 
#      ou seja, é possível que nessa situação a mensagem do flash reporte sucesso
#      no cadastro, ao passo que a mensagem do JS afirme "email inválido", visto 
#      que o file .py não tem a verificação de formato de email, ao contrário do .JS

from flask import Flask, render_template, request, flash, redirect, url_for, session
        
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

        if not user or not email or not password: 
            flash('Todos os campos são obrigatórios!', 'danger')
        else:
            flash(f'Usuário {user} cadastrado com sucesso!', 'success')
            if 'dados' in session:
                session['dados'].append([user, email, password])
            else:
                session['dados'] = [[user, email, password]]

    return render_template('formulario.html')
                           
if __name__ == '__main__':
    app.run(debug=True)

