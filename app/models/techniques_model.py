from app.configs.database import db
from dataclasses import dataclass
from datetime import datetime



class Techniques(db.Model):
    __tablename__ = "techniques"

    id_technique: int
    nm_technique: str
    dt_start: datetime
    dt_end: datetime    
    ds_comment: str


    id_technique = db.Column(db.Integer, primary_key=True)
    nm_technique = db.Column(db.String(255), nullable=False)
    dt_start = db.Column(db.Date, nullable=False, default=datetime.now())
    dt_end = db.Column(db.Date, nullable=False)
    ds_comment = db.Column(db.String(1000), nullable=False)
    id_customer_record = db.Column(db.Integer, db.ForeignKey('customers_record.id_customer_record'), nullable=False)

    def __iter__(self):
        yield 'id_technique', self.id_technique
        yield 'nm_technique', self.nm_technique
        yield 'dt_start', self.dt_start
        yield 'dt_end', self.dt_end
        yield 'ds_comment', self.ds_comment
