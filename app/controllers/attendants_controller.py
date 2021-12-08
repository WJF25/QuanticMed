from flask import request, jsonify, current_app
import sqlalchemy
import psycopg2
from sqlalchemy import and_, or_
from app.models.attendants_model import Attendants
from sqlalchemy.exc import IntegrityError
from psycopg2.errorcodes import UNIQUE_VIOLATION, FOREIGN_KEY_VIOLATION
from app.controllers.verifications import verify_keys, is_numeric_data
from app.exc.excessoes import NumericError, PasswordMinLengthError, WrongKeyError
from ipdb import set_trace


def create_attendant():

    session = current_app.db.session

    try:
        data = request.get_json()

        verify_keys(data, "attendant", "post")
        is_numeric_data(
            data['nr_cpf'], data['nr_cellphone'], data['nr_telephone'])

        inserted_data = Attendants(**data)

        session.add(inserted_data)
        session.commit()

        return jsonify(inserted_data), 201

    except WrongKeyError as error:
        return jsonify({"Error": error.value}), 400
    except NumericError as error:
        return jsonify(error.value), 400
    except PasswordMinLengthError as error:
        return jsonify(error.value), 400
    except IntegrityError as e:
        if e.orig.pgcode == UNIQUE_VIOLATION:
            return {"error": "Cpf já cadastrado"}, 409
        if e.orig.pgcode == FOREIGN_KEY_VIOLATION:
            return {"error": "Clínica não cadastrada"}, 400


def update_attendant(id):
    session = current_app.db.session

    data = request.get_json()

    filtered_data = Attendants.query.get(id)
    if filtered_data is None:
        return {"erro": "Recepcionista não existe"}

    try:
        verify_keys(data, "attendant", "patch")

        for key, value in data.items():
            setattr(filtered_data, key, value)

        session.add(filtered_data)
        session.commit()
    except WrongKeyError as error:
        return jsonify({"erro": error.value}), 400
    except NumericError as error:
        return jsonify(error.value), 400
    except PasswordMinLengthError as error:
        return jsonify(error.value), 400
    except IntegrityError as e:
        if e.orig.pgcode == UNIQUE_VIOLATION:
            return {"erro": "Cpf já cadastrado"}, 409
        if e.orig.pgcode == FOREIGN_KEY_VIOLATION:
            return {"erro": "Clínica não cadastrada"}, 400

    return jsonify(filtered_data), 200


def delete_attendant(id):
    session = current_app.db.session

    filtered_data = Attendants.query.get(id)
    if filtered_data is None:
        return {"error": "Recepcionista não encontrado"}

    session.delete(filtered_data)
    session.commit()

    return '', 204
