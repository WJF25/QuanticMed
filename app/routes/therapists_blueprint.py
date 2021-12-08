from flask import Blueprint

from app.controllers.therapists_controller import create_therapist, delete_therapist, update_therapist


bp = Blueprint('therapist_bp', __name__, url_prefix='/therapist')

bp.post("")(create_therapist)
bp.patch("<int:id>")(update_therapist)
bp.delete("<int:id>")(delete_therapist)
