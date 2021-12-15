from flask import Blueprint

from app.controllers.rooms_controller import create_rooms, delete_room, update_room, get_rooms, get_room_by_id, get_room_by_status, get_room_schedule


bp = Blueprint('room_bp', __name__, url_prefix='/rooms')

bp.post("")(create_rooms)
bp.delete("/<int:room_id>")(delete_room)
bp.patch("/<int:room_id>")(update_room)
bp.get("")(get_rooms)
bp.get("/<int:room_id>")(get_room_by_id)
bp.get("/<room_status>")(get_room_by_status)
bp.get("/schedule/<int:id_room>")(get_room_schedule)