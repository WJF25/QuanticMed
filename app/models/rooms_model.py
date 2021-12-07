from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey


@dataclass
class Rooms(db.Model):
    __tablename__ = "rooms"

    nm_room: str
    # backref para receber o nome da especialidade

    id_room = Column(Integer, primary_key=True)
    nm_room = Column(String(50), nullable=False)
    id_specialty = Column(Integer, ForeignKey('Specialties.id_specialty'))
