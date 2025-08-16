from sqlalchemy import create_engine,String,Integer,Float,DateTime,Column,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from flask_login import UserMixin
from random import randint


Base = declarative_base()


class User(Base,UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    full_name = Column(String,nullable=False)
    email = Column(String,unique=True,nullable=False)
    phone = Column(Integer)
    password = Column(String,nullable=False)


class Shipments(Base): 
    __tablename__ = 'shipments'
    id = Column(Integer, primary_key=True)
    status = Column(String,default = 'Pending')
    tracking_number = Column(String,unique=True,default=str(randint(1000000000,9999999999)))
    pickup_address = Column(String)
    pickup_city = Column(String)
    delivery_address = Column(String)
    delivery_city = Column(String)
    sender_name = Column(String)
    receiver_name = Column(String)
    sender_phone = Column(Integer)
    receiver_phone = Column(Integer)
    special_notes = Column(String)
    courier_type = Column(String)
    package_weight = Column(Float)
    collected_amount = Column(Float)
    shipment_cost = Column(Float)
    shipment_date = Column(DateTime)
    shipment_status = Column(String)
    pickup_date = Column(DateTime)
    delivery_date = Column(DateTime)
    warehouse_date= Column(DateTime)
    courier_type = Column(String)
    special_notes = Column(String)
    user_email = Column(String)
class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    wallet_id = Column(Integer, ForeignKey('wallet.id'), nullable=False)
    shipment_id = Column(Integer, ForeignKey('shipments.id'), nullable=True) # Can be null for wallet top-ups/withdrawals not tied to a specific shipment
    amount = Column(Float, nullable=False) # Positive for top-up, negative for payment
    transaction_type = Column(String(50), nullable=False) # e.g., 'Payment', 'Top-up', 'Withdrawal'
    timestamp = Column(DateTime, default=datetime.utcnow)
    description = Column(String(255))





class Wallet(Base):
    __tablename__ = 'wallet'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=True, nullable=False) # One-to-one with Users
    balance = Column(Float, default=0.0, nullable=False)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
db_session = Session()
    