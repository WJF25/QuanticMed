from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import backref, relationship
from datetime import datetime
import sqlalchemy
from app.models.clinics_model import Clinics
db: sqlalchemy = db


@dataclass
class Attendants(db.Model):

    nm_attendant: str
    nr_cpf: str
    nr_telephone: str
    nr_cellphone: str
    ds_password: str
    dt_creation_time: str
    id_clinic: int
    clinic: Clinics

    __tablename__ = 'attendants'

    id_attendant = db.Column(db.Integer, primary_key=True)
    nm_attendant = db.Column(db.String(50), nullable=False)
    nr_cpf = db.Column(db.String(11), nullable=False, unique=True)
    nr_telephone = db.Column(db.String(11))
    nr_cellphone = db.Column(db.String(11))
    ds_password = db.Column(db.String(15))
    dt_creation_time = db.Column(db.DateTime, default=datetime.now())
    id_clinic = db.Column(db.Integer, db.ForeignKey('clinics.id_clinic'))

    clinic = relationship('Clinics', backref=backref(
        'attendants', uselist=True), uselist=False)

    def __iter__(self):
        yield 'id_attendant', self.id_attendant
        yield 'nm_attendant', self.nm_attendant
        yield 'nr_cpf', self.nr_cpf
        yield 'nr_telephone', self.nr_telephone
        yield 'nr_cellphone', self.nr_cellphone
        yield 'ds_password', self.ds_password
        yield 'dt_creation_time', self.dt_creation_time
        yield 'id_clinic', self.id_clinic
        yield 'clinic', self.clinic
