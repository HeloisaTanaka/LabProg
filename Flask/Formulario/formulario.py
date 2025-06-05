from flask import Flask, render_template

app = Flask(__name__)

@forms.route('/')

def dados(nome, idade, endereco, email, cpf):
    return render_template('index.html', nome=nome, idade=idade, endereco=endereco, email=email, cpf=cpf)

if __name__=='__main__':
    app.run(debug=True)