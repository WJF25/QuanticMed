from app.configs.database import db
from dataclasses import dataclass
import sqlalchemy
db: sqlalchemy = db

@dataclass
class specialty(db.Model):

    nm_especialty: str

    __tablename__ = 'specialties'

    id_especialty  = db.Column(db.Integer, primary_key = True)
    nm_especialty = db.Column(db.String(50), nullable=False, unique=True)

    def __iter__(self):
        yield 'id_especialty', self.id_especialty
        yield 'nm_especialty', self.nm_especialty