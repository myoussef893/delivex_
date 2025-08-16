# auth.py
from models import db_session, User # Import User model
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager,login_user,current_user,logout_user
from app import app,render_template,redirect,url_for,flash
from forms import SignupForm, LoginForm


login_manager = LoginManager() # Initialize LoginManager
login_manager.init_app(app) # Initialize with your app
login_manager.login_view = 'signin' # Set the login view

@login_manager.user_loader # User loader callback
def load_user(user_id):
    return db_session.query(User).get(int(user_id))

@app.route('/signup',methods=['GET','POST'])
def signup(): 
    form = SignupForm()
    if form.validate_on_submit():
        new_user = User(
            full_name=form.full_name.data,
            email=form.email.data,
            phone=form.phone.data,
            password=generate_password_hash(form.password.data)
        )
        db_session.add(new_user)
        db_session.commit()
        print('Successfully added')
        return redirect(url_for("signin"))    

    return render_template('website/signup.html',form=form)

@app.route('/login', methods=["GET", "POST"])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user = db_session.query(User).filter_by(email=form.email.data).first()
        submitted_password = form.password.data

        # Check if user exists and password is correct.
        if user and check_password_hash(pwhash=user.password, password=submitted_password):
            login_user(user)
            # You can uncomment this line for debugging, but it's not necessary for the logic.
            return redirect(url_for('client_portal'))
        else:
            # This block is executed if the user is not found or the password is incorrect.
            flash('Wrong email or password.')
            return redirect(url_for('signin'))
    else: 
        print('Form is not validated.')
    # This line is reached for GET requests or if form validation fails.
    return render_template('website/login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('signin'))