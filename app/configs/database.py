from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.attendants_model import Attendants
    from app.models.clinics_model import Clinics
    from app.models.therapists_model import Therapists
    from app.models.locations_model import Locations
    from app.models.rooms_model import Rooms
    from app.models.specialties_model import Specialties
    from app.models.therapists_specialties_table_model import therapists_specialties_table
    from app.models.customers_model import Customers
    from app.models.customers_records_model import CustomersRecords
    from app.models.techniques_model import Techniques
    from app.models.sessions_table_model import sessions_table
    from app.models.sessions_model import Sessions