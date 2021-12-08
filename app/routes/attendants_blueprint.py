from flask import Blueprint

from app.controllers.attendants_controller import create_attendant

bp = Blueprint('attendant_bp', __name__, url_prefix='/attendant')

bp.post("")(create_attendant)
