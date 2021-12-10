from app.configs.database import db
from dataclasses import dataclass
import sqlalchemy
from sqlalchemy.orm import validates
from app.exc.excessoes import NumericError
db: sqlalchemy = db


@dataclass
class Address(db.Model):

    id_address: int
    ds_street: str
    nr_number: str
    ds_district: str
    ds_complement: str
    nr_zipcode: str
    ds_city: str
    ds_uf: str

    __tablename__ = 'address'

    id_address = db.Column(db.Integer, primary_key=True)
    ds_street = db.Column(db.String(40), nullable=False)
    nr_number = db.Column(db.String(10), nullable=False)
    ds_district = db.Column(db.String(20))
    ds_complement = db.Column(db.String(20))
    nr_zipcode = db.Column(db.String(10))
    ds_city = db.Column(db.String(30), nullable=False)
    ds_uf = db.Column(db.String(2), nullable=False)

    def __iter__(self):
        yield "id_address", self.id_address
        yield "ds_street", self.ds_street
        yield "nr_number", self.nr_number
        yield "ds_district", self.ds_district
        yield "ds_complement", self.ds_complement
        yield "nr_zipcode", self.nr_zipcode
        yield "ds_city", self.ds_city
        yield "ds_uf", self.ds_uf

    @validates('ds_street', 'ds_district', 'ds_complement', 'ds_city', 'ds_uf')
    def is_string(self, key, value):
        if type(value) is not str:
            raise TypeError(
                'Algum deste campos não é do tipo string: ds_street,  ds_district, ds_complement, ds_city, ds_uf')
        return value

    @validates('ds_street', 'ds_district', 'ds_complement', 'ds_city')
    def title_name(self, key, value):
        return value.title()

    @validates('ds_uf')
    def title_name(self, key, value):
        return value.upper()

    @validates('nr_number', 'nr_zipcode')
    def title_name(self, key, value):
        value = str(value)
        if not value.isnumeric() and not value == '':
            raise NumericError(
                {"message": "As chaves nr_number, nr_zipcode devem ser numéricas", "error": f"O valor {value} não é numérico"})
        return value
