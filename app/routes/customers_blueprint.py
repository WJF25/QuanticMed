from flask import Blueprint
from app.controllers.customers_controller import (
    create_customer,
    update_customer_by_id,
    delete_customer_by_id,
    get_customers,
    get_customer_by_id,
    get_customers_appointments,
    get_customer_records,
)

bp = Blueprint("customer_bp", __name__, url_prefix="/customers")
bp.post("")(create_customer)
bp.patch("/<int:id_customer>")(update_customer_by_id)
bp.delete("/<int:id_customer>")(delete_customer_by_id)
bp.get("")(get_customers)
bp.get("/<int:id_customer>")(get_customer_by_id)
bp.get("/<int:id_customer>/sessions")(get_customers_appointments)
bp.get("/<int:id_customer>/customer_records")(get_customer_records)
