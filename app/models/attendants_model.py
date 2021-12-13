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

    clinic = relationship('Clinics', backref=backref(
        'attendants', uselist=True), uselist=False)

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

    @validates('nm_attendant')
    def title_name(self, key, value):
        return value.title()

    @validates('ds_email')
    def check_email(self, key, value):
        pattern = r'^[\w]+@[\w]+\.[\w]{2,4}'
        if not re.match(pattern, value):
            raise EmailError({'erro': 'E-mail inválido'})
        return value

    @validates('nr_cpf', 'nr_cellphone', 'nr_telephone')
    def is_numeric_data(self, key, value):
        value = str(value)
        if not value.isnumeric() and not value == '':
            raise NumericError(
                {"message": "As chaves nr_cpf, nr_cellphone, nr_telephone devem ser numéricas", "error": f"O valor {value} não é numérico"})
        return value

    @property
    def ds_password(self):
        raise AttributeError('password is not a readable attribute')

    @ds_password.setter
    def ds_password(self, password_to_hash):
        self.ds_hash_password = generate_password_hash(password_to_hash)

    def check_password(self, password_to_check):
        return check_password_hash(self.ds_hash_password, password_to_check)
