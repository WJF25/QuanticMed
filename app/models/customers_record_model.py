from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class CustomersRecord(db.Model):

    __tablename__ = "customers_record"

    id_customer_record: int

    id_customer_record = Column(Integer, primary_key=True)
    id_customer = Column(Integer, ForeignKey(
        "customers.id_customer"), nullable=False)
    ds_comment = Column(String(1000), nullable=False)

    customer = relationship("Customer", backref=backref(
        "record", uselist=False), uselist=False)
