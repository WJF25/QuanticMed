from flask import Blueprint

from app.controllers.rooms_controller import create_rooms, delete_room, update_room


bp = Blueprint('room_bp', __name__, url_prefix='/rooms')

bp.post("")(create_rooms)
bp.delete("/<int:room_id>")(delete_room)
bp.patch("/<int:room_id>")(update_room)