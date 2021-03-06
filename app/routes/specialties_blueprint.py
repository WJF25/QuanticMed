from flask import Blueprint
from app.controllers.specialities_controller import create_specialty, update_specialty_by_id, delete_specialty, get_specialties

bp = Blueprint('specialties_bp', __name__, url_prefix='/specialties')

bp.post("")(create_specialty)
bp.patch("<int:specialty_id>")(update_specialty_by_id)
bp.delete("<int:specialty_id>")(delete_specialty)
bp.get("")(get_specialties)