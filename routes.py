from flask import render_template, url_for, request, redirect,flash
from app import app
from forms import * 
from models import Shipments,User
from shipments import * 
from flask_bootstrap import Bootstrap4
from werkzeug.security import check_password_hash, generate_password_hash
from auth import * 
from flask_login import login_required
bootstrap = Bootstrap4(app)

@app.route('/')
def home():
    return render_template('website/home.html')


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
        return redirect(url_for("/signin"))    

    return render_template('website/signup.html',form=form)

@app.route('/login',methods= ["GET","POST"])
def signin():
    form = LoginForm()
    error = None
    if form.validate_on_submit(): 
        user = db_session.query(User).filter_by(email = form.email.data).first()
        submitted_password = form.password.data

        if user:
            password = user.password
            if check_password_hash(pwhash=password,password=submitted_password):
                login_user(user)
                print(current_user.email) 

                return redirect('/client_portal')
        else: 
            error = flash('Wrong email or password.')
            print('Wrong email or password.')
            return redirect('/login')

    return render_template('website/login.html',form=form,error=error,user=current_user)




@app.route('/dashboard')
def employee_dashboard(): 
    return render_template('employee_view/employee_dashboard.html')

@login_required
@app.route('/client_portal')
def client_portal(): 
    return render_template('client_view/client_portal.html')

@app.route('/create_new_package',methods=['GET','POST'])
def new_package(): 
    form = NewPackageForm()
    if form.validate_on_submit():
        try:
            
            create_new_package(form,Shipments) 
            print('Successfully added')
            redirect(url_for("/client_portal"))
            
        except Exception as e: 
            print(e)
        
    return render_template('client_view/new_package_request.html',form=form)