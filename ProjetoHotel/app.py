from flask import Flask, render_template, session, redirect, url_for
from controllers.users_controller import user_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.register_blueprint(user_bp)

@app.route('/')
def pgindex():
    if 'usuario_logado' not in session:
        return render_template('login.html')
    id_user = session.get('usuario_logado')
    perfil = session.get('perfil')
    return render_template('index.html', perfil = perfil)

@app.route('/cadastro')
def pgCadastro():
    return render_template('cadastro.html')

@app.route('/login')
def pgLogin():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)