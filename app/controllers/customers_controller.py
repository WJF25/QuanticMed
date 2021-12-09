from flask import request, jsonify, current_app
from psycopg2.errors import UniqueViolation, NotNullViolation
from sqlalchemy.exc import IntegrityError
from app.exc.customers_errors import CustomerInvalidCpf, CustomerNotFoundError
from app.exc.excessoes import NumericError, WrongKeyError
from app.models.customers_model import Customers
from app.controllers.verifications import verify_keys, is_numeric_data


def create_customer():
    customer_data: dict = request.get_json()
    session = current_app.db.session

    try:
        verify_keys(customer_data, "customer", "post")
        is_numeric_data(
            customer_data["nr_cpf"],
            customer_data["nr_rg"],
            customer_data["nr_telephone"],
            customer_data["nr_cellphone"],
        )
        customer = Customers(**customer_data)
        session.add(customer)
        session.commit()

        return jsonify(customer), 201
    except NumericError as E:
        return jsonify(E.value), 400
    except CustomerInvalidCpf as E:
        return jsonify(E.value)
    except IntegrityError as E:
        if isinstance(E.orig, UniqueViolation):
            return {"erro": "cliente já cadastrado no banco de dados"}, 409
    except WrongKeyError as E:
        return jsonify({"Erro": E.value}), 400
    return {"erro": "Desculpe, nós não entendemos sua requisição"}, 400


def update_customer_by_id(id_customer):

    session = current_app.db.session
    data_to_update: dict = request.get_json()
    request_keys = list(data_to_update.keys())

    if len(request_keys) < 0:
        return {"message": "Invalid Body request"}, 400
    try:
        verify_keys(data_to_update, "customer", "patch")
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
    except WrongKeyError as E:
        return jsonify({"erro": E.value}), 400
    except IntegrityError as E:
        if isinstance(E.orig, UniqueViolation):
            return {"erro": "cliente já cadastrado no banco de dados"}, 409


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
