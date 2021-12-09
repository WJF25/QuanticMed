from flask import Blueprint

from app.controllers.attendants_controller import create_attendant, delete_attendant, get_all_attendants, update_attendant, get_attendant_by_id

bp = Blueprint('attendant_bp', __name__, url_prefix='/attendants')

bp.get("")(get_all_attendants)
bp.get("<int:id>")(get_attendant_by_id)
bp.post("")(create_attendant)
bp.patch("<int:id>")(update_attendant)
bp.delete("<int:id>")(delete_attendant)
