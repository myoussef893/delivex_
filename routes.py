from flask import render_template, url_for, request, redirect,flash
from app import app
from forms import * 
from models import Shipments,User,Wallet
from shipments import * 
from flask_bootstrap import Bootstrap4
from werkzeug.security import check_password_hash, generate_password_hash
from auth import * 
from flask_login import login_required,LoginManager,current_user,login_user,logout_user
from sqlalchemy import func
bootstrap = Bootstrap4(app)

@app.route('/')
def home():
    return render_template('website/home.html')

@app.route('/dashboard')
def employee_dashboard(): 
    return render_template('employee_view/employee_dashboard.html')

@login_required
@app.route('/client_portal')
def client_portal(): 
    return render_template('client_view/client_portal.html')

@login_required
@app.route('/create_new_package',methods=['GET','POST'])
def new_package(): 
    form = NewPackageForm()
    if form.validate_on_submit():
        try:
            create_new_package(form,Shipments) 
            print('Successfully added')
            redirect(url_for("client_portal"))
        except Exception as e: 
            print(e)
    return render_template('client_view/new_package_request.html',form=form)

@login_required
@app.route('/view_shipments',methods=['GET','POST'])
def view_shipments(): 
    shipments = db_session.query(Shipments).filter(Shipments.user_email == current_user.email).all()
    return render_template('client_view/my_shipments.html',shipments=shipments)

@app.route('/client_dashboard')
@login_required
def client_dashboard():
    # 1. Get wallet balance
    wallet = db_session.query(Wallet).filter_by(user_id=current_user.id).first()
    wallet_balance = wallet.balance if wallet else 0.0

    # 2. Calculate total shipments this month
    first_day = datetime(datetime.today().year, datetime.today().month, 1)
    total_shipments_month = db_session.query(Shipments).filter(
        Shipments.user_email == current_user.email,
        Shipments.shipment_date >= first_day
    ).count()

    # 3. Delivered
    total_delivered = db_session.query(Shipments).filter_by(
        user_email=current_user.email,
        shipment_status="Delivered"
    ).count()

    # 4. En Route
    total_enroute = db_session.query(Shipments).filter_by(
        user_email=current_user.email,
        shipment_status="En Route"
    ).count()

    # 5. Total collected amount
    total_collected = db_session.query(
        func.sum(Shipments.collected_amount)
    ).filter(
        Shipments.user_email == current_user.email
    ).scalar() or 0

    # 6. Total fees
    total_fees = db_session.query(
        func.sum(Shipments.shipment_cost)
    ).filter(
        Shipments.user_email == current_user.email
    ).scalar() or 0

    return render_template(
        '/client_view/client_dashboard.html',
        wallet_balance=wallet_balance,
        total_shipments_month=total_shipments_month,
        total_delivered=total_delivered,
        total_enroute=total_enroute,
        total_collected=total_collected,
        total_fees=total_fees
    )