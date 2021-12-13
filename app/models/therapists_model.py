from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref, validates
from app.exc.excessoes import NumericError
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
    ds_password: str
    ds_status: str
    specialties: list

    __tablename__ = 'therapists'

    id_therapist = db.Column(db.Integer, primary_key=True)
    nm_therapist = db.Column(db.String(50), nullable=False)
    nr_cpf = db.Column(db.String(11), nullable=False, unique=True)
    nr_crm = db.Column(db.String(15), unique=True)
    nr_cellphone = db.Column(db.String(11))
    nm_user = db.Column(db.String(15), unique=True)
    ds_status = db.Column(db.String(15), default="ativo")
    ds_password = db.Column(db.String(15))
    ds_email = db.Column(db.String(50), nullable=False)
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
        yield 'ds_password', self.ds_password
        yield 'ds_status', self.ds_status
        yield 'specialties', self.specialties

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

    @validates('nr_cpf', 'nr_cellphone')
    def title_name(self, key, value):
        value = str(value)
        if not value.isnumeric() and not value == '':
            raise NumericError(
                {"message": "As chaves nr_cpf, nr_cellphone, nr_telephone devem ser numéricas", "error": f"O valor {value} não é numérico"})
        return value

    @property
    def password(self):
        raise AttributeError('Senha não é um atributo de leitura')

    @password.setter
    def password(self, password_to_hash):
        self.ds_password = generate_password_hash(password_to_hash)

    def check_password(self, password_to_check):
        return check_password_hash(self.ds_password, password_to_check)
