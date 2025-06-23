from flask import Flask, render_template, session, request, url_for, redirect

app = Flask(__name__)
app.secret_key = 'abcd'



@app.route('/logar', methods=['POST'])
def login():
    users = {'marcelinho': 123, 'renata': 456}
    username = request.form['username']
    password = request.form['password']
    
    for i in users:
        if username == i and password == users.get(i):
            session['username'] = username
            return render_template('profile.html')


@app.route('/')

def dados():
    return render_template('login.html')

if __name__=='__main__':
    app.run(debug=True)