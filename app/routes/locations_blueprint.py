from flask import Blueprint
from app.controllers.locations_controller import create_location


bp = Blueprint('location_bp', __name__, url_prefix='/locations')

bp.post("")(create_location)