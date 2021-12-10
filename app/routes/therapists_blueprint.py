from flask import Blueprint

from app.controllers.therapists_controller import create_therapist, delete_therapist, get_all_therapists, get_costumer_by_therapist, get_therapist_by_id, update_therapist


bp = Blueprint('therapist_bp', __name__, url_prefix='/therapists')

bp.get("")(get_all_therapists)
bp.get("<int:id>")(get_therapist_by_id)
bp.post("")(create_therapist)
bp.patch("<int:id>")(update_therapist)
bp.delete("<int:id>")(delete_therapist)
bp.get("<int:id_therapist>/<int:id_costumer>")(get_costumer_by_therapist)

