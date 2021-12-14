from app.configs.database import db
from dataclasses import dataclass
import sqlalchemy
from sqlalchemy.orm import validates
import re

from app.exc.excessoes import EmailError, NumericError
db: sqlalchemy = db


@dataclass
class Clinics(db.Model):

    id_clinic: int
    nm_clinic: str
    nr_cnpj: str
    ds_address: str
    nr_address: int
    ds_complement: str
    ds_district: str
    nr_zipcode: str
    ds_city: str
    ds_uf: str
    ds_email: str
    nr_telephone: str
    nr_cellphone: str

    __tablename__ = 'clinics'

    id_clinic = db.Column(db.Integer, primary_key=True)
    nm_clinic = db.Column(db.String(40), nullable=False)
    nr_cnpj = db.Column(db.String(15), nullable=False, unique=True)
    ds_address = db.Column(db.String(30), nullable=False)
    nr_address = db.Column(db.String(10), nullable=False)
    ds_complement = db.Column(db.String(20))
    ds_district = db.Column(db.String(20))
    nr_zipcode = db.Column(db.String(10))
    ds_city = db.Column(db.String(30))
    ds_uf = db.Column(db.String(2))
    ds_email = db.Column(db.String(30), unique=True)
    nr_telephone = db.Column(db.String(11))
    nr_cellphone = db.Column(db.String(11))

    def __iter__(self):
        yield "id_clinic", self.id_clinic
        yield "nm_clinic", self.nm_clinic
        yield "nr_cnpj", self.nr_cnpj
        yield "ds_address", self.ds_address
        yield "nr_address", self.nr_address
        yield "ds_complement", self.ds_complement
        yield "ds_district", self.ds_district
        yield "nr_zipcode", self.nr_zipcode
        yield "ds_city", self.ds_city
        yield "ds_uf", self.ds_uf
        yield "ds_email", self.ds_email
        yield "nr_telephone", self.nr_telephone
        yield "nr_cellphone", self.nr_cellphone

    @validates('nm_clinic', 'ds_address', 'ds_district', 'ds_city')
    def title_name(self, key, value):
        return value.title()

    @validates('ds_uf')
    def upper_uf(self, key, value):
        return value.upper()

    @validates('ds_email')
    def check_email(self, key, value):
        pattern = r'^[\w]+@[\w]+\.[\w]{2,4}$'
        if not re.match(pattern, value):
            raise EmailError({'erro': 'E-mail inválido'})
        return value

    @validates('nr_telephone')
    def check_telephone(self, key, value):
        pattern = r'\d{10}'
        if not re.match(pattern, value) and value != '':
            raise NumericError({'erro': 'Telefone residencial inválido'})
        return value

    @validates('nr_cpf')
    def check_cpf(self, key, value):
        pattern = r'^\d{11}$'
        if not re.match(pattern, value):
            raise NumericError({'erro': 'Cpf inválido'})
        return value

    @validates('nr_cnpj')
    def check_cnpj(self, key, value):
        pattern = r'^\d{14}$'
        if not re.match(pattern, value):
            raise NumericError({'erro': 'Cnpj inválido'})
        return value

    @validates('nr_cellphone')
    def check_cellphone(self, key, value):
        pattern = r'^\d{10,11}$'
        if not re.match(pattern, value) and value != '':
            raise NumericError({'erro': 'Telefone celular inválido'})
        return value

    @validates('nr_zipcode')
    def check_zipcode(self, key, value):
        pattern = r'^\d{8}$'
        if not re.match(pattern, value) and value != '':
            raise NumericError({'erro': 'CEP inválido'})
        return value

    @validates('nr_address')
    def check_address(self, key, value):
        pattern = r'^\d{1,9}$'
        if not re.match(pattern, value):
            raise NumericError({'erro': 'Número residencial inválido'})
        return value
