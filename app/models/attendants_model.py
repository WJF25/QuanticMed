from sqlalchemy.sql.schema import ForeignKey
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import backref, relationship
from datetime import datetime
import sqlalchemy
db: sqlalchemy = db

@dataclass
class Attendant(db.Model):

    nm_attendant: str
    nr_cpf:str
    nr_telres: str
    nr_telcel: str
    ds_pass: str
    dt_creation_time: datetime
    id_clinic: int

    __tablename__ = 'attendants'

    id_attendant  = db.Column(db.Integer, primary_key = True)
    nm_attendant = db.Column(db.String(50), nullable=False)
    nr_cpf = db.Column(db.String(11), nullable=False, unique=True)
    nr_telres = db.Column(db.String(11))
    nr_telcel = db.Column(db.String(11))
    ds_pass = db.Column(db.String(15))
    dt_creation_time = db.Column(db.DateTime)
    id_clinic = db.Column(db.Integer, db.ForeignKey('clinics.id_clinic'))

    clinic = relationship('Clinic', backref=backref('attendant', uselist=True), uselist=False)

    def __iter__(self):
        yield 'id_attendant', self.id_attendant
        yield 'nm_attendant', self.nm_attendant
        yield 'nr_cpf', self.nr_cpf
        yield 'nr_telres', self.nr_telres
        yield 'nr_telcel', self.nr_telcel
        yield 'ds_pass', self.ds_pass
        yield 'dt_creation_time', self.dt_creation_time
        yield 'id_clinic', self.id_clinic