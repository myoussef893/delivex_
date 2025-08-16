from flask import Flask
from flask_login import LoginManager
from models import User

login_manager = LoginManager()

app = Flask(__name__)
app.config['SECRET_KEY']= '1q2w3e4r5t6y7u8i9o0p'




from routes import * 
from auth import * 





if __name__ == '__main__':
    app.run(debug=True)