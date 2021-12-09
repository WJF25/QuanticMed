from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref, validates
from app.exc.excessoes import NumericError
from app.models.therapists_specialties_table_model import therapists_specialties_table
import sqlalchemy

db: sqlalchemy = db


@dataclass
class Therapists(db.Model):
    id_therapist: int
    nm_therapist: str
    nr_cpf: str
    nr_crm: str
    nr_cellphone: str
    nm_user: str
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

    specialties = relationship('Specialties', secondary=therapists_specialties_table, backref=backref(
        'therapists', uselist=True), uselist=True)

    def __iter__(self):
        yield 'id_therapist', self.id_therapist
        yield 'nm_therapist', self.nm_therapist
        yield 'nr_cpf', self.nr_cpf
        yield 'nr_crm', self.nr_crm
        yield 'nr_cellphone', self.nr_cellphone
        yield 'nm_user', self.nm_user
        yield 'ds_password', self.ds_password
        yield 'ds_status', self.ds_status
        yield 'specialties', self.specialties

    @validates('nm_attendant')
    def title_name(self, key, value):
        return value.title()

    @validates('nr_cpf', 'nr_cellphone')
    def title_name(self, key, value):
        if not value.isnumeric():
            raise NumericError(
                {"message": "As chaves nr_cpf, nr_cellphone, nr_telephone devem ser numericas", "error": f"O valor {value} não é numérico"})
        return value
