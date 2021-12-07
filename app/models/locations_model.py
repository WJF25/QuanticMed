from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref
from datetime import datetime

from app.models.rooms_model import Rooms


@dataclass
class Locations(db.Model):
    __tablename__ = "locations"

    dt_start: datetime
    dt_end: datetime
    room: Rooms
    # clinic: Clinics importar clinica model
    # therapist: Therapists importar model

    id_location = Column(Integer, primary_key=True)
    dt_start = Column(DateTime)
    dt_end = Column(DateTime)
    id_room = Column(Integer, ForeignKey("rooms.id_room"))
    id_clinic = Column(Integer, ForeignKey("clinics.id_clinic"))
    id_therapist = Column(Integer, ForeignKey("therapists.id_therapist"))

    room = relationship("Rooms", backref="locations", uselist=False)
    clinic = relationship("Clinics", uselist=False)
    therapists = relationship("Therapists", backref="locations", uselist=False)
