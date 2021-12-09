from flask import Blueprint

from app.controllers.clinics_controller import create_clinic, delete_clinic, get_clinics, get_clinics_by_id, update_clinic

bp = Blueprint('clinic_bp', __name__, url_prefix='/clinics')

bp.get("")(get_clinics)
bp.get("<int:id>")(get_clinics_by_id)
bp.post("")(create_clinic)
bp.patch("<int:id>")(update_clinic)
bp.delete("<int:id>")(delete_clinic)