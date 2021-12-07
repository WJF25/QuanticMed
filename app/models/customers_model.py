from app.models.sessions_table_model import sessions
from datetime import datetime
from sqlalchemy.orm import backref, relationship
from app.configs.database import db
from dataclasses import dataclass
import sqlalchemy
db: sqlalchemy = db


@dataclass
class Customers(db.Model):
    id_customer: int
    nm_customer: str
    nr_cpf: str
    nr_rg: str
    nm_mother: str
    nm_father: str
    nr_work_permit: str
    ds_adress: str
    nr_phone_res: str
    nr_phone_ces: str
    ds_email: str
    id_report: int
    dt_birthdate: datetime

    __tablename__ = 'customers'

    id_customer = db.Column(db.Integer, primary_key=True),
    nm_customer = db.Column(db.String(50), nullable=False),
    nr_cpf = db.Column(db.String(11), nullable=False, unique=True),
    nr_rg = db.Column(db.String(11), nullable=False, unique=True),
    nm_mother = db.Column(db.String(50), nullable=True),
    nm_father = db.Column(db.String(50), nullable=True),
    nr_work_permit = db.Column(db.String(11), nullable=True, unique=True),
    ds_adress = db.Column(db.String(50), nullable=False),
    nr_phone_res = db.Column(db.String(11), nullable=True, unique=True),
    nr_phone_ces = db.Column(db.String(11), nullable=True, unique=True),
    ds_email = db.Column(db.String(50), nullable=True, unique=True)
    id_report = db.Column(db.Integer, db.ForeignKey('reports.id_report')),
    dt_birthdate = db.Column(db.Date, nullable=False)

    appointments = relationship(
        'Therapist',
        secondary=sessions,
        backref=backref('customers', uselist=False)
    )

    def __iter__(self):
        yield 'id_customer', self.id_customer
        yield 'nm_customer', self.nm_customer
        yield 'nr_cpf', self.nr_cpf
        yield 'nr_rg', self.nr_rg
        yield 'nm_mother', self.nm_mother
        yield 'nm_father', self.nm_father
        yield 'nr_work_permit', self.nr_work_permit
        yield 'ds_adress', self.ds_adress
        yield 'nr_phone_res', self.nr_phone_res
        yield 'nr_phone_ces', self.nr_phone_ces
        yield 'ds_email', self.ds_email
        yield 'id_report', self.id_report
        yield 'dt_birthdate', self.dt_birthdate
