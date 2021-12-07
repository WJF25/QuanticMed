from sqlalchemy.sql.sqltypes import String
from app.configs.database import db
from dataclasses import dataclass
import sqlalchemy

db: sqlalchemy = db


@dataclass
class Therapist(db.Model):
    id_medico: int
    nm_medico: str
    nr_cpf: str
    nr_crm: str
    ds_area: str
    nm_usuario: str
    ds_senha: str
    fl_admin: str
    nr_acessos: int

    id_medico = db.Column(db.Integer, primary_key=True),
    nm_medico = db.Column(db.String(50), nullable=False),
    nr_cpf = db.Column(db.String(11), nullable=False),
    nr_crm = db.Column(db.String(15), nullable=False),
    ds_area = db.Column(db.String(20), nullable=False),
    nm_usuario = db.Column(db.String(15), nullable=False),
    ds_senha = db.Column(db.String(15), nullable=False),
    fl_admin = db.Column(db.String(3), nullable=True),
    nr_acessos = db.Column(db.Integer, nullable=True)

    def __iter__(self):
        yield 'id_medico', self.id_medico
        yield 'nm_medico', self.nm_medico
        yield 'nr_cpf', self.nr_cpf
        yield 'nr_crm', self.nr_crm
        yield 'ds_area', self.ds_area
        yield 'nm_usuario', self.nm_usuario
        yield 'ds_senha', self.ds_senha
        yield 'fl_admin', self.fl_admin
        yield 'nr_acessos', self.nr_acessos
