from flask import Flask
from flask_login import LoginManager
from models import User

login_manager = LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY']= 'SECRET'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




from routes import * 





if __name__ == '__main__':
    app.run(debug=True)