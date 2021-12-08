from flask import json, request, jsonify, current_app
from psycopg2.errors import UniqueViolation, NotNullViolation
from sqlalchemy.exc import IntegrityError
from app.exc.customers_errors import CustomerInvalidCpf, CustomerNotFoundError
from app.models.customers_model import Customers
import re


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
    customer_data: dict = request.get_json()
    request_keys = list(customer_data.keys())
    session = current_app.db.session
    Customers.delete_invalid_keys(request_keys, valid_keys, customer_data)
    keys = list(customer_data.keys())
    Customers.get_missing_keys(keys, valid_keys, missing_keys)
    customer = Customers(**customer_data)
    cpf = customer_data["nr_cpf"]
    rg = customer_data["nr_rg"]
    try:
        if len(cpf) != 11 or len(rg) != 11:
            raise CustomerInvalidCpf({"msg": "cpf and rg field must have 11 digits"})
    except CustomerInvalidCpf as E:
        return jsonify(E.value)
    try:
        session.add(customer)
        session.commit()

        return jsonify(customer), 201
    except IntegrityError as E:
        if isinstance(E.orig, UniqueViolation):
            return {"msg": "Customer already exists in the database"}, 409
        if isinstance(E.orig, NotNullViolation):
            return {
                "msg": "You have missing keys in you body request",
                "valid_keys": valid_keys,
                "missing_keys": missing_keys,
            }, 400
    return {"msg": "I'm sorry, we did not understand your request"}, 400


def update_customer_by_id(id_customer):
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
    session = current_app.db.session
    data_to_update: dict = request.get_json()
    request_keys = list(data_to_update.keys())
    Customers.delete_invalid_keys(request_keys, valid_keys, data_to_update)
    new_keys = list(data_to_update.keys())
    if len(new_keys):
        return {"message": "Invalid Body request"}, 400
    try:
        customer_found = Customers.query.filter_by(id_customer=id_customer).update(
            data_to_update
        )
        if not customer_found:
            raise CustomerNotFoundError({"msg": "customer not found"})
        session.commit()
        new_costumer = Customers.query.get(id_customer)
        return jsonify(new_costumer), 200
    except CustomerNotFoundError as E:
        return jsonify(E.value), 404


def delete_customer_by_id(id_customer):
    session = current_app.db.session
    try:
        cate_to_deleted = Customers.query.filter_by(
            id_customer=id_customer
        ).one_or_none()
        if not cate_to_deleted:
            raise CustomerNotFoundError({"msg": "customer not found"})
        session.delete(cate_to_deleted)
        session.commit()
        return "", 204
    except CustomerNotFoundError as E:
        return jsonify(E.value), 404
