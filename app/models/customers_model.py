from datetime import datetime
from sqlalchemy.orm import backref, relationship, validates
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
    nr_healthcare: str
    ds_address: str
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
    nr_healthcare = db.Column(db.String(30), unique=True)
    ds_address = db.Column(db.String(50), nullable=False)
    nr_telephone = db.Column(db.String(11))
    nr_cellphone = db.Column(db.String(11))
    ds_email = db.Column(db.String(50))
    dt_birthdate = db.Column(db.String(10), nullable=False)
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
        yield "nr_telephone", self.nr_telephone
        yield "nr_cellphone", self.nr_cellphone
        yield "ds_email", self.ds_email
        yield "dt_birthdate", self.dt_birthdate
        # yield 'id_report', self.id_report

    @validates("nm_customer")
    def title_name(self, key, value):
        return value.title()

    @validates("ds_email")
    def lower_email(self, key, value: str):
        return value.lower()
