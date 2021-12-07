from app.configs.database import db
from dataclasses import dataclass
import sqlalchemy
db: sqlalchemy = db

@dataclass
class Speciality(db.Model):

    nm_especiality: str

    __tablename__ = 'specialities'

    id_especiality  = db.Column(db.Integer, primary_key = True)
    nm_especiality = db.Column(db.String(50), nullable=False, unique=True)

    def __iter__(self):
        yield 'id_especiality', self.id_especiality
        yield 'nm_especiality', self.nm_especiality