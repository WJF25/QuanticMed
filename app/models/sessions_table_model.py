from app.configs.database import db
from dataclasses import dataclass
import sqlalchemy
db: sqlalchemy = sqlalchemy

sessions = db.Table(
    id_consulta=db.Column(db.Integer),
    id_paciente=db.Column(db.Integer, db.ForeignKey(
        'Customer.id_customer')),
    id_medico=db.Column(db.Integer, db.ForeignKey('Therapist.id_medic')),
    dt_inicio=db.Column(db.DateTime, nullable=False),
    dt_fim=db.Column(db.DateTime, nullable=False),
    ds_status=db.Column(db.String(15))

)
