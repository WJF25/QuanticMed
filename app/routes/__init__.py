from flask import Flask

from app.routes.customer_blueprint import bp as bp_customer
from app.routes.location_blueprint import bp as bp_location
from app.routes.room_blueprint import bp as bp_room
from app.routes.therapist_blueprint import bp as bp_therapist
from app.routes.attendant_blueprint import bp as bp_attendant


def init_app(app: Flask):
    app.register_blueprint(bp_customer)
    app.register_blueprint(bp_location)
    app.register_blueprint(bp_room)
    app.register_blueprint(bp_therapist)
    app.register_blueprint(bp_attendant)