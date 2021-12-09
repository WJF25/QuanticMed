from flask import request, jsonify, current_app
import sqlalchemy
import psycopg2
from sqlalchemy import and_, or_
from app.models.clinics_model import Clinics
from sqlalchemy.exc import IntegrityError
from psycopg2.errorcodes import UNIQUE_VIOLATION, FOREIGN_KEY_VIOLATION
from app.controllers.verifications import verify_keys, is_numeric_data
from app.exc.excessoes import NumericError, PasswordMinLengthError, WrongKeyError


def create_clinic():

    session = current_app.db.session

    try:
        data = request.get_json()

        verify_keys(data, "clinic", "post")

        inserted_data = Clinics(**data)

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
            return {"error": "Cnpj ou email já cadastrados"}, 409

        
def update_clinic(id):

    session = current_app.db.session

    data = request.get_json()

    filtered_data = Clinics.query.get(id)

    if filtered_data is None:
        return {"erro": "Clinica não existe"}

    try:
        verify_keys(data, "clinic", "patch")

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
            return {"erro": "Cnpj ou email já cadastrados"}, 409

    return jsonify(filtered_data), 200


def delete_clinic(id):

        session = current_app.db.session

        filtered_data = Clinics.query.get(id)
        if filtered_data is None:
            return {"error": "Clinica não encontrada"}

        session.delete(filtered_data)
        session.commit()

        return "", 204


def get_clinics_by_id(id):
    clinic = Clinics.query.filter_by(id_clinic=id).first()
    if clinic is None:
        return jsonify({"erro": "Clínica não existe"}), 404
    return jsonify(clinic)


def get_clinics():
    clinic = Clinics.query.all()

    return jsonify(clinic)