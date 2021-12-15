from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import backref, relationship, validates
from datetime import datetime
import sqlalchemy
from app.models.clinics_model import Clinics
from app.exc.excessoes import NumericError, EmailError
import re
from werkzeug.security import generate_password_hash, check_password_hash
db: sqlalchemy = db


@dataclass
class Attendants(db.Model):

    id_attendant: str
    nm_attendant: str
    nr_cpf: str
    nr_telephone: str
    nr_cellphone: str
    ds_email: str
    dt_creation_time: str
    id_clinic: int
    fl_admin: str

    __tablename__ = 'attendants'

    id_attendant = db.Column(db.Integer, primary_key=True)
    nm_attendant = db.Column(db.String(50), nullable=False)
    nr_cpf = db.Column(db.String(11), nullable=False, unique=True)
    nr_telephone = db.Column(db.String(11))
    nr_cellphone = db.Column(db.String(11))
    ds_hash_password = db.Column(db.String(255))
    ds_email = db.Column(db.String(40), unique=True, nullable=False)
    dt_creation_time = db.Column(db.DateTime, default=datetime.now())
    id_clinic = db.Column(db.Integer, db.ForeignKey('clinics.id_clinic'))
    fl_admin = db.Column(db.String(3), nullable=False, default='ATD')

    def __iter__(self):
        yield 'id_attendant', self.id_attendant
        yield 'nm_attendant', self.nm_attendant
        yield 'nr_cpf', self.nr_cpf
        yield 'nr_telephone', self.nr_telephone
        yield 'nr_cellphone', self.nr_cellphone
        yield 'ds_email', self.ds_email
        yield 'dt_creation_time', self.dt_creation_time
        yield 'id_clinic', self.id_clinic
        yield 'clinic', self.clinic
        yield 'fl_admin', self.fl_admin

    @validates('nm_attendant')
    def title_name(self, key, value):
        return value.title()

    @validates('ds_email')
    def check_email(self, key, value):
        pattern = r'^[\w]+@[\w]+\.[\w]{2,4}$'
        if not re.match(pattern, value):
            raise EmailError({'erro': 'E-mail inválido. Formato válido: usuario@email.com'})
        return value

    @validates('nr_telephone')
    def check_telephone(self, key, value):
        pattern = r'^\d{10}$'
        if not re.match(pattern, value) and value != '':
            raise NumericError({'erro': 'Telefone residencial inválido. Formato válido: 10 dígitos numéricos.'})
        return value

    @validates('nr_cpf')
    def check_cpf(self, key, value):
        pattern = r'^\d{11}$'
        if not re.match(pattern, value):
            raise NumericError({'erro': 'Cpf inválido. Formato válido: 11 dígitos númericos.'})
        return value

    @validates('nr_cellphone')
    def check_cellphone(self, key, value):
        pattern = r'^\d{10,11}$'
        if not re.match(pattern, value) and value != '':
            raise NumericError({'erro': 'Telefone celular inválido. Formato válido: 10-11 dígitos numéricos.'})
        return value

    @property
    def ds_password(self):
        raise AttributeError('password is not a readable attribute')

    @ds_password.setter
    def ds_password(self, password_to_hash):
        self.ds_hash_password = generate_password_hash(password_to_hash)

    def check_password(self, password_to_check):
        return check_password_hash(self.ds_hash_password, password_to_check)
