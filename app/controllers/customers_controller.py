from flask import request, jsonify, current_app
from psycopg2.errors import UniqueViolation, NotNullViolation
from sqlalchemy.exc import IntegrityError
from app.models.customers_model import Customers


def create_customer():
    missing_keys = []
    valid_keys = [
        "nm_customer",
        "nr_cpf",
        "nr_rg",
        "nm_mother",
        "nm_father",
        "nr_healthcare",
        "ds_address",
        "nr_telephone",
        "nr_cellphone",
        "ds_email",
        "dt_birthdate",
    ]
    customer_data = request.get_json()
    request_keys = list(customer_data.keys())
    session = current_app.db.session
    Customers.delete_invalid_keys(request_keys, valid_keys, customer_data)
    keys = list(customer_data.keys())
    Customers.get_missing_keys(keys, valid_keys, missing_keys)
    customer = Customers(**customer_data)
    try:
        session.add(customer)
        session.commit()
        return jsonify(customer), 200
    except IntegrityError as E:
        if isinstance(E.orig, UniqueViolation):
            return {"msg": "Customer already exists in the database"}, 409
        if isinstance(E.orig, NotNullViolation):
            return {
                "msg": "You have missing keys in you body request",
                "valid_keys": valid_keys,
                "missing_keys": missing_keys,
            }, 400
    return {"msg": "I'm sorry, we did not understand your request"}

    def update_customer_by_id(customer_id):
        ...
