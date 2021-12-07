from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref
from app.models.therapists_specialties_table_model import therapists_specialties_table
import sqlalchemy

db: sqlalchemy = db


@dataclass
class Therapists(db.Model):
    id_therapist: int
    nm_therapist: str
    nr_cpf: str
    nr_crm: str    
    nm_user: str
    ds_password: str
    specialties: list
    

    __tablename__ = 'therapists'

    id_therapist = db.Column(db.Integer, primary_key=True)
    nm_therapist = db.Column(db.String(50), nullable=False)
    nr_cpf = db.Column(db.String(11), nullable=False, unique=True)
    nr_crm = db.Column(db.String(15), unique=True)
    nm_user = db.Column(db.String(15), unique=True)
    ds_password = db.Column(db.String(15))

    specialties = relationship('Specialties', secondary=therapists_specialties_table, backref=backref('therapists', uselist=True), uselist=True)
    


    def __iter__(self):
        yield 'id_therapist', self.id_therapist
        yield 'nm_therapist', self.nm_therapist
        yield 'nr_cpf', self.nr_cpf
        yield 'nr_crm', self.nr_crm        
        yield 'nm_user', self.nm_user
        yield 'ds_password', self.ds_password
        yield 'specialties', self.specialties      
        
