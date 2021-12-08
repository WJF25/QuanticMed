from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import relationship
from app.models.specialties_model import Specialties
import sqlalchemy
db: sqlalchemy = db


@dataclass
class Rooms(db.Model):
    __tablename__ = "rooms"

    id_room: int
    nm_room: str
    specialty: Specialties

    id_room = db.Column(db.Integer, primary_key=True)
    nm_room = db.Column(db.String(50), nullable=False)
    id_specialty = db.Column(db.Integer, db.ForeignKey('specialties.id_specialty'))

    specialty = relationship("Specialties", uselist=False)

    def __iter__(self):
        yield 'id_room', self.id_room
        yield 'nm_room', self.nm_room
        yield 'id_specialty', self.id_specialty
