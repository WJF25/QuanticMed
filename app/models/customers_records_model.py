from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship, backref
from app.models.customers_model import Customers
import sqlalchemy
db: sqlalchemy = db


@dataclass
class CustomersRecords(db.Model):

    __tablename__ = "customers_records"

    id_customer_record: int
    id_customer:int
    customer: Customers

    id_customer_record = db.Column(db.Integer, primary_key=True)
    id_customer = db.Column(db.Integer, db.ForeignKey(
        "customers.id_customer"), nullable=False)

    customer = relationship("Customers", backref=backref(
        "record", uselist=False), uselist=False)

    def __iter__(self):
        yield 'id_customer_record', self.id_customer_record
        yield 'id_customer', self.id_customer
        yield 'customer', self.customer
