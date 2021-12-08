from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.orm import eagerload, relationship, backref
from datetime import datetime
from app.models.rooms_model import Rooms
from app.models.therapists_model import Therapists
from app.models.clinics_model import Clinics
import sqlalchemy
db: sqlalchemy = db


@dataclass
class Locations(db.Model):
    __tablename__ = "locations"
    id_location: int
    dt_start: datetime
    dt_end: datetime
    room: list 
    clinic: Clinics
    therapists: Therapists

    id_location = db.Column(db.Integer, primary_key=True)
    dt_start = db.Column(db.DateTime, nullable=False)
    dt_end = db.Column(db.DateTime)
    id_room = db.Column(db.Integer, db.ForeignKey("rooms.id_room"))
    id_clinic = db.Column(db.Integer, db.ForeignKey("clinics.id_clinic"))
    id_therapist = db.Column(db.Integer, db.ForeignKey("therapists.id_therapist"))

    room = relationship("Rooms", backref=backref("locations", uselist=True), uselist=False)
    clinic = relationship("Clinics", uselist=False)
    therapists = relationship("Therapists", backref=backref("locations", uselist=True), uselist=False)

    def __iter__(self):
        yield "id_location", self.id_location
        yield "dt_start", self.dt_start
        yield "dt_end", self.dt_end
        yield "room", self.room
        yield "clinic", self.clinic
        yield "therapist", self.therapists
