from app.models.sessions_table_model import sessions
from datetime import date
from sqlalchemy.orm import relationship
from app.configs.database import db
from dataclasses import dataclass
import sqlalchemy
db: sqlalchemy = db


@dataclass
class CustomersModel(db.Model):
    id_paciente: int
    nm_paciente: str
    nr_cpf: str
    nr_rg: str
    nm_mae: str
    nm_pai: str
    nr_carteora: str
    ds_endereco: str
    nr_telefone_res: str
    nr_telefone_ces: str
    ds_email: str
    id_laudo: int
    dt_data_nasc: date

    id_paciente = db.Column(db.Integer, primary_key=True),
    nm_paciente = db.Column(db.String(50), nullable=False),
    nr_cpf = db.Column(db.String(11), nullable=False),
    nr_rg = db.Column(db.String(11), nullable=False),
    nm_mae = db.Column(db.String(50), nullable=True),
    nm_pai = db.Column(db.String(50), nullable=True),
    nr_carteora = db.Column(db.String(11), nullable=True),
    ds_endereco = db.Column(db.String(50), nullable=False),
    nr_telefone_res = db.Column(db.String(11), nullable=True),
    nr_telefone_ces = db.Column(db.String(11), nullable=True),
    ds_email = db.Column(db.String(50), nullable=True)
    id_laudo = db.Column(db.Integer, db.ForeignKey('LaudosModel.id_laudo')),
    dt_data_nasc = db.Column(db.Date, nullable=False)

    consultas = relationship(
        'TherapistModel',
        secondary=sessions,
        backref='consultas'
    )
