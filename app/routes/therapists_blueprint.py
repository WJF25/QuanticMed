from flask import Blueprint

from app.controllers.therapists_controller import create_therapist


bp = Blueprint('therapist_bp', __name__, url_prefix='/therapist')

bp.post("")(create_therapist)
