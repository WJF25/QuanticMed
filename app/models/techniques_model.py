from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime
import sqlalchemy
from sqlalchemy.orm import relationship, backref

db: sqlalchemy = db


@dataclass
class Techniques(db.Model):
    __tablename__ = "techniques"

    nm_technique: str
    dt_start: datetime
    dt_end: datetime
    ds_comment: str
    id_therapist: int
    id_customer_record: int

    id_technique = db.Column(db.Integer, primary_key=True)
    nm_technique = db.Column(db.String(50), nullable=False)
    dt_start = db.Column(db.Date, nullable=False, default=datetime.now())
    dt_end = db.Column(db.Date)
    ds_comment = db.Column(db.String(1000))
    id_customer_record = db.Column(
        db.Integer,
        db.ForeignKey("customers_records.id_customer_record"),
        nullable=False,
    )
    id_therapist = db.Column(
        db.Integer, db.ForeignKey("therapists.id_therapist"), nullable=False
    )

    therapist = relationship("Therapists", backref="techniques", uselist=False)

    def __iter__(self):
        yield "id_technique", self.id_technique
        yield "nm_technique", self.nm_technique
        yield "dt_start", self.dt_start
        yield "dt_end", self.dt_end
        yield "ds_comment", self.ds_comment
        yield "id_customer_record", self.id_customer_record
        yield "id_therapists", self.id_therapists
