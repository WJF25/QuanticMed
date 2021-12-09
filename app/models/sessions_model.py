from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import validates
import sqlalchemy
db: sqlalchemy = db


@dataclass
class Sessions(db.Model):
    id_session: int
    id_customer: int
    id_therapist: int
    dt_start: str
    dt_end: str
    ds_status: str

    __tablename__ = 'sessions'

    id_session = db.Column(db.Integer, primary_key=True)
    id_customer = db.Column(db.Integer, db.ForeignKey('customers.id_customer'))
    id_therapist = db.Column(
        db.Integer, db.ForeignKey('therapists.id_therapist'))
    dt_start = db.Column(db.DateTime(), nullable=False)
    dt_end = db.Column(db.DateTime())
    ds_status = db.Column(db.String(15))

    def __iter__(self):
        yield 'id_session', self.id_session
        yield 'id_customer', self.id_customer
        yield 'id_therapist', self.id_therapist
        yield 'dt_start', self.dt_start
        yield 'dt_end', self.dt_end
        yield 'ds_status', self.ds_status

    @validates('ds_status')
    def title_name(self, key, value):
        return value.title()