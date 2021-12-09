from flask import Flask

from app.routes.customers_blueprint import bp as bp_customer
from app.routes.locations_blueprint import bp as bp_location
from app.routes.rooms_blueprint import bp as bp_room
from app.routes.therapists_blueprint import bp as bp_therapist
from app.routes.attendants_blueprint import bp as bp_attendant
from app.routes.specialties_blueprint import bp as bp_specialties
from app.routes.sessions_blueprint import bp as bp_session
from app.routes.clinics_blueprint import bp as bp_clinics


def init_app(app: Flask):
    app.register_blueprint(bp_customer)
    app.register_blueprint(bp_location)
    app.register_blueprint(bp_room)
    app.register_blueprint(bp_therapist)
    app.register_blueprint(bp_attendant)
    app.register_blueprint(bp_specialties)
    app.register_blueprint(bp_session)
    app.register_blueprint(bp_clinics)