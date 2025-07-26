# auth.py
from models import db_session, User # Import User model
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager,login_user,current_user
from app import app # Import app from your main Flask application instance


login_manager = LoginManager() # Initialize LoginManager
login_manager.init_app(app) # Initialize with your app
login_manager.login_view = 'signin' # Set the login view

@login_manager.user_loader # User loader callback
def load_user(user_id):
    return db_session.query(User).get(int(user_id))


def create_new_user(form, model):
    new_user = model(
        full_name=form.full_name.data,
        email=form.email.data,
        phone=form.phone.data,
        password=generate_password_hash(form.password.data, method='sha256') # salt_length is deprecated
    )
    db_session.add(new_user)
    db_session.commit()


def login_user_auth(form, model): # Renamed to avoid conflict with Flask-Login's login_user
    user = db_session.query(model).filter_by(email=form.email.data).first()
    if user and check_password_hash(form.password.data, user.password):
        print('Password is correct')
        return login_user(user)
    else: 
        return "Invalid Password"