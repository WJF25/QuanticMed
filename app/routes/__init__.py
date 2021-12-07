from flask import Flask

from app.routes.customers_blueprint import bp as bp_customer
from app.routes.locations_blueprint import bp as bp_location
from app.routes.rooms_blueprint import bp as bp_room
from app.routes.therapists_blueprint import bp as bp_therapist
from app.routes.attendants_blueprint import bp as bp_attendant
from app.routes.specialities_blueprint import bp as bp_specialities
from app.routes.sessions_blueprint import bp as bp_session


def init_app(app: Flask):
    app.register_blueprint(bp_customer)
    app.register_blueprint(bp_location)
    app.register_blueprint(bp_room)
    app.register_blueprint(bp_therapist)
    app.register_blueprint(bp_attendant)
    app.register_blueprint(bp_specialities)
    app.register_blueprint(bp_session)