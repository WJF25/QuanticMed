from app.configs.database import db
from dataclasses import dataclass
import sqlalchemy
db: sqlalchemy = sqlalchemy

session = db.Table(
    id_consulta=db.Column(db.Integer),
    id_paciente=db.Column(db.Integer, db.ForeignKey(
        'CustomerModel.id_paciente')),
    id_medico=db.Column(db.Integer, db.ForeignKey('TherapistModel.id_medico')),
    dt_inicio=db.Column(db.DateTime, nullable=False),
    dt_fim=db.Column(db.DateTime, nullable=False),
    ds_status=db.Column(db.String(15))

)
