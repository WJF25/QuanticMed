import re
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref, validates
from app.exc.excessoes import EmailError, NumericError
from app.models.therapists_specialties_table_model import therapists_specialties_table
import sqlalchemy
from werkzeug.security import generate_password_hash, check_password_hash

db: sqlalchemy = db


@dataclass
class Therapists(db.Model):
    id_therapist: int
    nm_therapist: str
    nr_cpf: str
    nr_crm: str
    nr_cellphone: str
    nm_user: str
    ds_email: str
    ds_status: str
    fl_admin: str
    specialties: list

    __tablename__ = 'therapists'

    id_therapist = db.Column(db.Integer, primary_key=True)
    nm_therapist = db.Column(db.String(50), nullable=False)
    nr_cpf = db.Column(db.String(11), nullable=False, unique=True)
    nr_crm = db.Column(db.String(15), unique=True)
    nr_cellphone = db.Column(db.String(11))
    nm_user = db.Column(db.String(15), unique=True)
    ds_status = db.Column(db.String(15), default="ativo")
    ds_hash_password = db.Column(db.String(255))
    ds_email = db.Column(db.String(50), nullable=False, unique=True)
    fl_admin = db.Column(db.String(3), nullable=False, default='TRP')

    specialties = relationship('Specialties', secondary=therapists_specialties_table, backref=backref(
        'therapists', uselist=True), uselist=True)

    def __iter__(self):
        yield 'id_therapist', self.id_therapist
        yield 'nm_therapist', self.nm_therapist
        yield 'nr_cpf', self.nr_cpf
        yield 'nr_crm', self.nr_crm
        yield 'nr_cellphone', self.nr_cellphone
        yield 'nm_user', self.nm_user
        yield 'ds_email', self.ds_email
        yield 'ds_status', self.ds_status
        yield 'fl_admin', self.fl_admin
        yield 'specialties', self.specialties

    @validates('nm_therapist')
    def title_name(self, key, value):
        return value.title()

    @validates('ds_email')
    def check_email(self, key, value):
        pattern = r'^[\w]+@[\w]+\.[\w]{2,4}'
        if not re.match(pattern, value):
            raise EmailError({'erro': 'E-mail inválido'})
        return value

    @validates('ds_status')
    def normalize_status(self, key, value):
        return value.lower()

    @validates('nr_cpf')
    def check_cpf(self, key, value):
        pattern = r'^\d{11}$'
        if not re.match(pattern, value):
            raise NumericError({'erro': 'Cpf inválido'})
        return value

    @validates('nr_cellphone')
    def check_cellphone(self, key, value):
        pattern = r'^\d{10,11}$'
        if not re.match(pattern, value) and value != '':
            raise NumericError({'erro': 'Telefone celular inválido'})
        return value

    @validates('nr_crm')
    def check_crm(self, key, value):
        pattern = r'^\d{4,10}\/[A-Z]{2}$'
        if not re.match(pattern, value):
            raise NumericError({'erro': 'CRM inválido'})
        return value

    @property
    def ds_password(self):
        raise AttributeError('password is not a readable attribute')

    @ds_password.setter
    def ds_password(self, password_to_hash):
        self.ds_hash_password = generate_password_hash(password_to_hash)

    def check_password(self, password_to_check):
        return check_password_hash(self.ds_hash_password, password_to_check)
