from flask import Blueprint
from app.controllers.sessions_controller import create_appointment, update_appointment_by_id, delete_appointment


bp = Blueprint('sessions_bp', __name__, url_prefix='/sessions')

bp.post("")(create_appointment)
bp.patch("<int:session_id>")(update_appointment_by_id)
bp.delete("<int:session_id>")(delete_appointment)