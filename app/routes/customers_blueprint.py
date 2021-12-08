from flask import Blueprint
from app.controllers.customers_controller import create_customer

bp = Blueprint('customer_bp', __name__, url_prefix='/customers')
bp.post("")(create_customer)
