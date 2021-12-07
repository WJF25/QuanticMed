from app.configs.database import db
from dataclasses import dataclass
import sqlalchemy
db: sqlalchemy = db


@dataclass
class Specialty(db.Model):

    nm_specialty: str

    __tablename__ = 'specialties'

    id_specialty = db.Column(db.Integer, primary_key=True)
    nm_specialty = db.Column(db.String(50), nullable=False, unique=True)

    def __iter__(self):
        yield 'id_specialty', self.id_specialty
        yield 'nm_specialty', self.nm_specialty