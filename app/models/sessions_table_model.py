from app.configs.database import db
import sqlalchemy
db: sqlalchemy = db

sessions_table = db.Table('sessions_table',
    db.Column('id_session', db.Integer, primary_key=True),
    db.Column('id_customer', db.Integer, db.ForeignKey('customers.id_customer')),
    db.Column('id_therapist', db.Integer, db.ForeignKey('therapists.id_therapist')),
    db.Column('dt_start', db.DateTime, nullable=False),
    db.Column('dt_end', db.DateTime),
    db.Column('ds_status', db.String(15)))