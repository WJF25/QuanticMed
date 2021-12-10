from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import backref, relationship, validates
from datetime import datetime
import sqlalchemy
from app.models.clinics_model import Clinics
from app.exc.excessoes import NumericError
db: sqlalchemy = db


@dataclass
class Attendants(db.Model):

    id_attendant: str
    nm_attendant: str
    nr_cpf: str
    nr_telephone: str
    nr_cellphone: str
    ds_password: str
    ds_email: str
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
    ds_email = db.Column(db.String(40))
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
        yield 'ds_email', self.ds_email
        yield 'dt_creation_time', self.dt_creation_time
        yield 'id_clinic', self.id_clinic
        yield 'clinic', self.clinic

    @validates('nm_attendant', 'ds_password', 'ds_email')
    def is_string(self, key, value):
        if type(value) is not str:
            raise TypeError(
                'Algum deste campos não é do tipo string nm_attendant, ds_password,ds_email')
        return value

    @validates('nm_attendant')
    def title_name(self, key, value):
        return value.title()

    @validates('de_email')
    def title_name(self, key, value):
        return value.lower()

    @validates('nr_cpf', 'nr_cellphone', 'nr_telephone')
    def title_name(self, key, value):
        value = str(value)
        if not value.isnumeric() and not value == '':
            raise NumericError(
                {"message": "As chaves nr_cpf, nr_cellphone, nr_telephone devem ser numéricas", "error": f"O valor {value} não é numérico"})
        return value
