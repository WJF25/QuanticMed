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
from sqlalchemy import and_
from flask_jwt_extended import jwt_required
from app.controllers.login_controller import only_role
from sqlalchemy.orm.exc import StaleDataError


@only_role('ATD')
@jwt_required()
def create_customer():
    session = current_app.db.session
    customer_data: dict = request.get_json()

    try:
        verify_keys(customer_data, "customer", "post")

        customer = Customers(**customer_data)
        session.add(customer)
        session.commit()

        customer_record = CustomersRecords(
            **{"id_customer": customer.id_customer})
        session.add(customer_record)
        session.commit()

    except DataError as e:
        if e.orig.pgcode == STRING_DATA_RIGHT_TRUNCATION:
            return {"error": "Valor mais longo que o permitido"}, 400
    except EmailError as E:
        return jsonify(E.value), 400
    except IntegrityError as E:
        if isinstance(E.orig, UniqueViolation):
            return {"erro": "Rg ou cpf já cadastrado no banco de dados"}, 409
    except NumericError as E:
        return jsonify(E.value), 400
    except WrongKeyError as E:
        return jsonify({"Erro": E.value}), 400
    response = dict(customer)
    return jsonify(response), 201


@only_role('ATD')
@jwt_required()
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


@only_role('ATD')
@jwt_required()
def delete_customer_by_id(id_customer):
    session = current_app.db.session
    try:
        customer = Customers.query.filter_by(id_customer=id_customer).first()
        if customer == None:
            raise CustomerNotFoundError({"erro": "Cliente não encontrado"})
        session.delete(customer)
        session.commit()
        return "", 204
    except CustomerNotFoundError as E:
        return jsonify(E.value), 404
    except StaleDataError:
        return jsonify({"Error": "Esta cliente é chave estrageira de outra entidade."}), 405


@only_role('ATD')
@jwt_required()
def get_customers():
    session = current_app.db.session
    name = request.args.get('name', '').title()
    if name:
        query_filter = and_((Customers.nm_customer.contains(name)))
        customers = Customers.query.filter(query_filter).all()
        if not customers:
            return {"erro": "Cliente não encontrado"}, 404
        return jsonify(customers), 200

    customers = Customers.query.all()
    if not customers:
        return {"erro": "Nenhum cliente encontrado"}, 404
    return jsonify(customers), 200


@only_role('ATD')
@jwt_required()
def get_customer_by_id(id_customer):
    customer = Customers.query.filter_by(id_customer=id_customer).one_or_none()
    if not customer:
        return {"erro": "Cliente não encontrado"}, 404
    return jsonify(customer), 200


@only_role('ATD')
@jwt_required()
def get_customers_appointments(id_customer):
    session = current_app.db.session
    customer = session.query(Customers).filter_by(
        id_customer=id_customer).one_or_none()
    if not customer:
        return {"erro": "Cliente não encontrado"}, 404
    dict_costumer = dict(customer)
    del dict_costumer["id_customer"]
    sessions = Sessions.query.filter_by(id_customer=id_customer).all()
    if len(sessions) < 1:
        return {"erro": "Não há sessões para este cliente"}, 404
    dict_costumer["sessões"] = sessions
    return jsonify(dict_costumer), 200


@only_role('TRP')
@jwt_required()
def get_customer_records(id_customer):
    session = current_app.db.session
    customer_record = (
        session.query(CustomersRecords).filter_by(
            id_customer=id_customer).one_or_none()
    )
    if not customer_record:
        return {"erro": "Prontuário não encontrado"}, 404
    customer = (
        session.query(Customers)
        .filter_by(id_customer=customer_record.id_customer)
        .one_or_none()
    )
    new_costumer = dict(customer)
    new_costumer["id_customer_record"] = customer_record.id_customer_record
    new_costumer["customer_records"] = []
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
