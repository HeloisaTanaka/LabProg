from flask import Flask, render_template
from controllers.users_controller import user_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'
app.register_blueprint(user_bp)





if __name__ == '__main__':
    app.run(debug=True)