from app.configs.database import db
from dataclasses import dataclass


@dataclass
class Clinics(db.Model):

    id_clinic: int
    nm_clinic: str
    nr_cnpj: str
    ds_specialties: str
    ds_address: str
    nr_number: int
    ds_complement: str
    ds_district: str
    nr_cep: str
    ds_city: str
    ds_uf: str
    ds_email: str
    nr_telephone: str
    nr_cellphone: str

    __tablename__ = 'clinics'

    id_clinic = db.Column(db.Integer, primary_key=True),
    nm_clinic = db.column(db.String(40), nullable=False),
    nr_cnpj = db.Column(db.String(15), nullable=False, unique=True),
    ds_specialties = db.Column(db.String(50), nullable=False),
    ds_address = db.Column(db.String(30), nullable=False),
    nr_number = db.Column(db.Integer, nullable=False),
    ds_complement = db.Column(db.String(20), nullable=False),
    ds_district = db.Column(db.String(20), nullable=False),
    nr_cep = db.Column(db.String(10), nullable=False),
    ds_city = db.Column(db.String(20), nullable=False),
    ds_uf = db.Column(db.String(2), nullable=False),
    ds_email = db.Column(db.String(30), nullable=False, unique=True),
    nr_telephone = db.Column(db.String(11), nullable=False),
    nr_cellphone = db.Column(db.String(11), nullable=False)

    def __iter__(self):
        yield "id_clinic", self.id_clinic
        yield "nm_clinic", self.nm_clinic
        yield "nr_cnpj", self.nr_cnpj
        yield "ds_specialties", self.ds_specialties
        yield "ds_address", self.ds_address
        yield "nr_number", self.nr_number
        yield "ds_complement", self.ds_complement
        yield "ds_district", self.ds_district
        yield "nr_cep", self.nr_cep
        yield "ds_city", self.ds_city
        yield "ds_uf", self.ds_uf
        yield "ds_email", self.ds_email
        yield "nr_telephone", self.nr_telephone
        yield "nr_cellphone", self.nr_cellphone
