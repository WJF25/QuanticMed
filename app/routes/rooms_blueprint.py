from flask import Blueprint

from app.controllers.rooms_controller import create_rooms


bp = Blueprint('room_bp', __name__, url_prefix='/rooms')

bp.post("")(create_rooms)