from flask import Blueprint
from app.controllers.locations_controller import create_location, delete_location, update_location, get_locations, get_locations_by_id


bp = Blueprint('location_bp', __name__, url_prefix='/locations')

bp.post("")(create_location)
bp.delete("<int:location_id>")(delete_location)
bp.patch("<int:location_id>")(update_location)
bp.get("")(get_locations)
bp.get("<int:location_id>")(get_locations_by_id)