from flask import Blueprint
from app.controllers.locations_controller import create_location, delete_location, get_location_by_clinic, update_location, get_locations, get_locations_by_id, get_location_by_therapist


bp = Blueprint('location_bp', __name__, url_prefix='/locations')

bp.post("")(create_location)
bp.delete("<int:location_id>")(delete_location)
bp.patch("<int:location_id>")(update_location)
bp.get("")(get_locations)
bp.get("<int:location_id>")(get_locations_by_id)
bp.get("/therapist/<int:therapist_id>")(get_location_by_therapist)
bp.get("/clinic/<int:clinic_id>")(get_location_by_clinic)
