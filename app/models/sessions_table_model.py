from app.configs.database import db
from dataclasses import dataclass
import sqlalchemy
db: sqlalchemy = sqlalchemy

sessions = db.Table(
    id_appointment=db.Column(db.Integer, primary_key=True),
    id_customer=db.Column(db.Integer, db.ForeignKey(
        'CustomerModel.id_paciente')),
    id_medic=db.Column(db.Integer, db.ForeignKey('TherapistModel.id_medico')),
    dt_start=db.Column(db.DateTime, nullable=False),
    dt_end=db.Column(db.DateTime, nullable=False),
    ds_status=db.Column(db.String(15))

)
