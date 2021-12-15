from datetime import datetime
from sqlalchemy.orm import backref, relationship, validates
from app.configs.database import db
from dataclasses import dataclass
import sqlalchemy
import re
from app.exc.excessoes import EmailError, NumericError

db: sqlalchemy = db


@dataclass
class Customers(db.Model):

    id_customer: int
    nm_customer: str
    nr_cpf: str
    nr_rg: str
    nm_mother: str
    nm_father: str
    nr_healthcare: str
    ds_address: str
    nr_address: str
    nr_zipcode: str
    nr_telephone: str
    nr_cellphone: str
    ds_email: str
    dt_birthdate: str

    __tablename__ = "customers"

    id_customer = db.Column(db.Integer, primary_key=True)
    nm_customer = db.Column(db.String(50), nullable=False)
    nr_cpf = db.Column(db.String(11), nullable=False, unique=True)
    nr_rg = db.Column(db.String(11), unique=True)
    nm_mother = db.Column(db.String(50))
    nm_father = db.Column(db.String(50))
    nr_healthcare = db.Column(db.String(30))
    ds_address = db.Column(db.String(50), nullable=False)
    nr_address = db.Column(db.String(10), nullable=False)
    nr_zipcode = db.Column(db.String(10))
    nr_telephone = db.Column(db.String(11))
    nr_cellphone = db.Column(db.String(11))
    ds_email = db.Column(db.String(50))
    dt_birthdate = db.Column(db.Date, nullable=False)
    # id_report = db.Column(db.Integer, db.ForeignKey('reports.id_report')),

    appointments = relationship(
        "Therapists",
        secondary="sessions",
        backref=backref("customers", uselist=False),
        uselist=True,
    )

    def __iter__(self):
        yield "id_customer", self.id_customer
        yield "nm_customer", self.nm_customer
        yield "nr_cpf", self.nr_cpf
        yield "nr_rg", self.nr_rg
        yield "nm_mother", self.nm_mother
        yield "nm_father", self.nm_father
        yield "nr_healthcare", self.nr_healthcare
        yield "ds_address", self.ds_address
        yield "nr_address", self.nr_address
        yield "nr_zipcode", self.nr_zipcode
        yield "nr_telephone", self.nr_telephone
        yield "nr_cellphone", self.nr_cellphone
        yield "ds_email", self.ds_email
        yield "dt_birthdate", self.dt_birthdate
        # yield 'id_report', self.id_report

    @validates("nm_customer", 'nm_father', "nm_mother", "ds_address")
    def title_name(self, key, value):
        return value.title()

    @validates('ds_email')
    def check_email(self, key, value):
        pattern = r'^[^\@\s]+@[\w]+\.[\w]{2,4}$'
        if not re.match(pattern, value):
            raise EmailError({'erro': 'E-mail inválido. Formato válido: usuario@email.com'})
        return value

    @validates('nr_telephone')
    def check_telephone(self, key, value):
        pattern = r'\d{10}'
        if not re.match(pattern, value) and value != '':
            raise NumericError({'erro': 'Telefone residencial inválido. Formato válido: 10 dígitos numéricos.'})
        return value

    @validates('nr_cpf')
    def check_cpf(self, key, value):
        pattern = r'^\d{11}$'
        if not re.match(pattern, value):
            raise NumericError({'erro': 'Cpf inválido. Formato válido: 11 dígitos numéricos.'})
        return value

    @validates('nr_cellphone')
    def check_cellphone(self, key, value):
        pattern = r'^\d{10,11}$'
        if not re.match(pattern, value) and value != '':
            raise NumericError({'erro': 'Telefone celular inválido. Formato válido: 10-11 dígitos numéricos.'})
        return value

    @validates('nr_zipcode')
    def check_zipcode(self, key, value):
        pattern = r'^\d{8}$'
        if not re.match(pattern, value) and value != '':
            raise NumericError({'erro': 'CEP inválido. Formato válido: 8 dígitos numéricos.'})
        return value

    @validates('nr_address')
    def check_address(self, key, value):
        pattern = r'^\d{1,9}$'
        if not re.match(pattern, value):
            raise NumericError({'erro': 'Número residencial inválido. Formato válido: 1-9 dígitos numéricos.'})
        return value

    @validates('nr_rg')
    def check_rg(self, key, value):
        pattern = r'^\d{6,15}$'
        if not re.match(pattern, value):
            raise NumericError({'erro': 'Número de RG inválido. Formato válido: 6-15 dígitos numéricos.'})
        return value
    
    @validates('dt_birthdate')
    def check_telephone(self, key, value):
        pattern = r'\d{2}\/\d{2}\/\d{4}'
        if not re.match(pattern, value):
            raise NumericError({'erro': 'Data de nascimento inválida. Formato válido: 00/00/0000.'})
        if int(value[0:2]) > 12 or int(value[0:2]) < 1:
            raise NumericError({'erro': 'Data de nascimento inválida. Mês maior que 12 ou menor que 1.'})
        if int(value[3:5]) > 31 or int(value[3:5]) < 1:
            raise NumericError({'erro': 'Data de nascimento inválida. Dua maior que 31 ou menor que 1.'})
        return value
