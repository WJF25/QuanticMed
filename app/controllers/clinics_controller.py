from flask import request, jsonify, current_app
from app.models.clinics_model import Clinics
from sqlalchemy.exc import IntegrityError, DataError
from psycopg2.errorcodes import UNIQUE_VIOLATION, STRING_DATA_RIGHT_TRUNCATION
from app.controllers.verifications import verify_keys
from app.exc.excessoes import EmailError, NumericError, WrongKeyError
from flask_jwt_extended import jwt_required
from app.controllers.login_controller import only_role

@only_role('ATD')
@jwt_required()
def create_clinic():

    session = current_app.db.session

    try:
        data = request.get_json()

        verify_keys(data, "clinic", "post")

        inserted_data = Clinics(**data)

        session.add(inserted_data)
        session.commit()

        return jsonify(inserted_data), 201
    except DataError as e:
        if e.orig.pgcode == STRING_DATA_RIGHT_TRUNCATION:
            return {"error": "Valor mais longo que o permitido"}, 400
    except EmailError as error:
        return jsonify(error.value), 400
    except IntegrityError as e:
        if e.orig.pgcode == UNIQUE_VIOLATION:
            return {"error": "Cnpj ou email já cadastrados"}, 409
    except NumericError as error:
        return jsonify(error.value), 400
    except WrongKeyError as error:
        return jsonify({"Error": error.value}), 400

@only_role('ATD')
@jwt_required()
def update_clinic(id):

    session = current_app.db.session

    data = request.get_json()

    filtered_data = Clinics.query.get(id)

    if filtered_data is None:
        return {"erro": "Clinica não existe"}, 404

    try:
        verify_keys(data, "clinic", "patch")

        for key, value in data.items():
            setattr(filtered_data, key, value)

        session.add(filtered_data)
        session.commit()
    except DataError as e:
        if e.orig.pgcode == STRING_DATA_RIGHT_TRUNCATION:
            return {"error": "Valor mais longo que o permitido"}, 400
    except EmailError as error:
        return jsonify(error.value), 400
    except IntegrityError as e:
        if e.orig.pgcode == UNIQUE_VIOLATION:
            return {"error": "Cnpj ou email já cadastrados"}, 409
    except NumericError as error:
        return jsonify(error.value), 400
    except WrongKeyError as error:
        return jsonify({"Error": error.value}), 400

    return jsonify(filtered_data), 200

@only_role('ATD')
@jwt_required()
def delete_clinic(id):

    session = current_app.db.session

    filtered_data = Clinics.query.get(id)
    if filtered_data is None:
        return {"error": "Clinica não encontrada"}, 404

    session.delete(filtered_data)
    session.commit()

    return "", 204

@only_role('ATD')
@jwt_required()
def get_clinics_by_id(id):
    clinic = Clinics.query.filter_by(id_clinic=id).first()
    if clinic is None:
        return jsonify({"erro": "Clínica não existe"}), 404
    return jsonify(clinic), 200

@only_role('ATD')
@jwt_required()
def get_clinics():
    clinic = Clinics.query.all()

    return jsonify(clinic), 200
