from app.configs.database import db
from dataclasses import dataclass


@dataclass
class Clinics(db.Model):

    id_clinic: int
    nm_clinic: str
    nr_cnpj: str
    ds_specialities: str
    ds_adress: str
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
    ds_specialities = db.Column(db.String(50), nullable=False),
    ds_adress = db.Column(db.String(30), nullable=False),
    nr_number = db.Column(db.Integer, nullable=False),
    ds_complement = db.Column(db.String(20), nullable=False),
    ds_district = db.Column(db.String(20), nullable=False),
    nr_cep = db.Column(db.String(10), nullable=False),
    ds_city = db.Column(db.String(20), nullable=False),
    ds_uf = db.Column(db.String(2), nullable=False),
    ds_email = db.Column(db.String(30), nullable=False, unique=True),
    nr_telephone = db.Column(db.String(11), nullable=False),
    nr_cellphone = db.Column(db.String(11), nullable=False)
