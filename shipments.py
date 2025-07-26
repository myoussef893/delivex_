from models import db_session
from datetime import datetime



def create_new_package(form,model):
    new_package = model(
        pickup_address=form.pickup_address.data,
        pickup_city=form.pickup_city.data,
        delivery_address=form.delivery_address.data,
        delivery_city=form.delivery_city.data,
        sender_name=form.sender_name.data,
        receiver_name=form.receiver_name.data,
        sender_phone=form.sender_phone.data,
        receiver_phone=form.receiver_phone.data,
        special_notes=form.special_notes.data,
        courier_type=form.courier_type.data,
        package_weight=form.package_weight.data,
        collected_amount=0.0,
        shipment_cost=0.0,
        shipment_date=datetime.utcnow(),
        shipment_status='Pending',
        pickup_date=None,
        delivery_date=None,
        warehouse_date=None
    )
    db_session.add(new_package)
    db_session.commit()



