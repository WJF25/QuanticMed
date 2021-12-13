from flask import request, jsonify, current_app
from psycopg2.errorcodes import STRING_DATA_RIGHT_TRUNCATION
from psycopg2.errors import UniqueViolation
from sqlalchemy.exc import DataError, IntegrityError
from app.exc.customers_errors import CustomerNotFoundError
from app.exc.excessoes import EmailError, NumericError, WrongKeyError
from app.models.customers_model import Customers
from app.controllers.verifications import verify_keys
from app.models.customers_records_model import CustomersRecords
from app.models.sessions_model import Sessions
from app.models.techniques_model import Techniques


def create_customer():
    customer_data: dict = request.get_json()
    session = current_app.db.session

    try:
        verify_keys(customer_data, "customer", "post")

        customer = Customers(**customer_data)
        session.add(customer)
        session.commit()

        return jsonify(customer), 201
    except DataError as e:
        if e.orig.pgcode == STRING_DATA_RIGHT_TRUNCATION:
            return {"error": "Valor mais longo que o permitido"}, 400
    except EmailError as E:
        return jsonify(E.value), 400
    except IntegrityError as E:
        if isinstance(E.orig, UniqueViolation):
            return {"erro": "cliente já cadastrado no banco de dados"}, 409
    except NumericError as E:
        return jsonify(E.value), 400
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
    except DataError as e:
        if e.orig.pgcode == STRING_DATA_RIGHT_TRUNCATION:
            return {"error": "Valor mais longo que o permitido"}, 400
    except EmailError as E:
        return jsonify(E.value), 400
    except IntegrityError as E:
        if isinstance(E.orig, UniqueViolation):
            return {"erro": "cliente já cadastrado no banco de dados"}, 409
    except NumericError as E:
        return jsonify(E.value), 400
    except WrongKeyError as E:
        return jsonify({"Erro": E.value}), 400


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


def get_customers():
    customers = Customers.query.all()
    session = current_app.db.session
    params: dict = dict(request.args)
    if params:
        customers = (
            session.query(Customers)
            .paginate(
                int(params.get("page", 1)),
                int(params.get("per_page", 15)),
                max_per_page=30,
            )
            .items
        )
        response = [dict(customer) for customer in customers]
        return jsonify(response)
    if len(customers) < 1:
        return {"erro": "Não achamos nada no nosso banco de dados"}, 404
    return jsonify(customers), 200


def get_customer_by_id(id_customer):
    customer = Customers.query.filter_by(id_customer=id_customer).one_or_none()
    if not customer:
        return {"erro": "Não achamos nada no nosso banco de dados"}, 200
    return jsonify(customer), 404


def get_customers_appointments(id_customer):
    session = current_app.db.session
    customer = session.query(Customers).filter_by(
        id_customer=id_customer).one_or_none()
    dict_costumer = dict(customer)
    del dict_costumer["id_customer"]
    if not customer:
        return {"erro": "Não achamos nada no nosso banco de dados"}
    sessions = Sessions.query.filter_by(id_customer=id_customer).all()
    if len(sessions) < 1:
        return {"erro": "Não achamos nada no nosso banco de dados"}, 404
    dict_costumer["sessões"] = sessions
    return dict_costumer, 200


def get_customer_records(id_customer):
    session = current_app.db.session
    customer_record = (
        session.query(CustomersRecords).filter_by(
            id_customer=id_customer).one_or_none()
    )
    if not customer_record:
        return {"erro": "Não achamos nada no nosso banco de dados"}, 404
    customer = (
        session.query(Customers)
        .filter_by(id_customer=customer_record.id_customer)
        .one_or_none()
    )
    new_costumer = dict(customer)
    new_costumer["customer_records"] = []
    del new_costumer["id_customer"]
    customer_records = (
        session.query(Customers, Techniques)
        .select_from(Customers)
        .join(CustomersRecords)
        .join(Techniques)
        .filter(Techniques.id_customer_record == customer_record.id_customer_record)
        .all()
    )
    records = [dict(record) for record in customer_records]
    for i in records:
        new_costumer["customer_records"].append(i["Techniques"])
    return jsonify(new_costumer), 200
