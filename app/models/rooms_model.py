from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref


@dataclass
class Rooms(db.Model):
    __tablename__ = "rooms"

    id_room: int
    nm_room: str
    # specialty: Specialties importar model

    id_room = Column(Integer, primary_key=True)
    nm_room = Column(String(50), nullable=False)
    id_specialty = Column(Integer, ForeignKey('Specialties.id_specialty'))

    specialty = relationship("Specialties", uselist=False)
