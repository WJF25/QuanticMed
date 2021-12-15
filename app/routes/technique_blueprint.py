from flask import Blueprint

from app.controllers.techniques_controller import create_technique, delete_technique, get_techniques, get_techniques_by_id, update_technique_by_id


bp = Blueprint('technique_bp', __name__, url_prefix='/techniques')

bp.get("")(get_techniques)
bp.get("/<int:technique_id>")(get_techniques_by_id)
bp.post("")(create_technique)
bp.patch("/<int:technique_id>")(update_technique_by_id)
bp.delete("/<int:technique_id>")(delete_technique)
