from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime
import sqlalchemy
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm import validates
import re
from app.exc.excessoes import NumericError
db: sqlalchemy = db


@dataclass
class Techniques(db.Model):
    __tablename__ = "techniques"

    id_technique: int
    nm_technique: str
    dt_start: str
    dt_end: str
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

    therapist = relationship('Therapists', backref='techniques', uselist=False)

    def __iter__(self):
        yield 'id_technique', self.id_technique
        yield 'nm_technique', self.nm_technique
        yield 'dt_start', self.dt_start
        yield 'dt_end', self.dt_end
        yield 'ds_comment', self.ds_comment
        yield 'id_customer_record', self.id_customer_record
        yield 'id_therapist', self.id_therapist

    @validates('nm_technique')
    def normalize_name(self, key, value):
        return value.title()

    @validates('dt_start', 'dt_end')
    def check_dates(self, key, value):
        pattern = r'\d{2}\/\d{2}\/\d{4}'
        if not re.match(pattern, value):
            raise NumericError(
                {'erro': 'Data inválida. Formato válido: 00/00/0000.'})
        if int(value[0:2]) > 12 or int(value[0:2]) < 1:
            raise NumericError(
                {'erro': 'Data inválida. Mês maior que 12 ou menor que 1.'})
        if int(value[3:5]) > 31 or int(value[3:5]) < 1:
            raise NumericError(
                {'erro': 'Data inválida. Dia maior que 31 ou menor que 1.'})
        return value