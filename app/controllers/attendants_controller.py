from flask import request, jsonify, current_app
import sqlalchemy
import psycopg2
from sqlalchemy import desc, asc, and_
from app.models.attendants_model import Attendants
from sqlalchemy.exc import DataError, IntegrityError
from psycopg2.errorcodes import STRING_DATA_RIGHT_TRUNCATION, UNIQUE_VIOLATION, FOREIGN_KEY_VIOLATION
from app.controllers.verifications import verify_keys
from app.exc.excessoes import NumericError, EmailError, WrongKeyError
from flask_jwt_extended import jwt_required
from app.controllers.login_controller import only_role

@only_role('ATD')
@jwt_required()
def create_attendant():

    session = current_app.db.session

    try:
        data = request.get_json()

        verify_keys(data, "attendant", "post")

        inserted_data = Attendants(**data)

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
            return {"error": "Cpf já cadastrado"}, 409
        if e.orig.pgcode == FOREIGN_KEY_VIOLATION:
            return {"error": "Clínica não cadastrada"}, 400
    except NumericError as error:
        return jsonify(error.value), 400
    except WrongKeyError as error:
        return jsonify({"Error": error.value}), 400

@only_role('ATD')
@jwt_required()
def update_attendant(id):
    session = current_app.db.session

    data = request.get_json()

    filtered_data = Attendants.query.get(id)
    if filtered_data is None:
        return {"erro": "Recepcionista não encontrado"}

    try:
        verify_keys(data, "attendant", "patch")

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
            return {"error": "Cpf já cadastrado"}, 409
        if e.orig.pgcode == FOREIGN_KEY_VIOLATION:
            return {"error": "Clínica não cadastrada"}, 400
    except NumericError as error:
        return jsonify(error.value), 400
    except WrongKeyError as error:
        return jsonify({"Error": error.value}), 400

    return jsonify(filtered_data), 200

@only_role('ATD')
@jwt_required()
def delete_attendant(id):
    session = current_app.db.session

    filtered_data = Attendants.query.get(id)
    if filtered_data is None:
        return {"error": "Recepcionista não encontrado"}

    session.delete(filtered_data)
    session.commit()

    return '', 204

@only_role('ATD')
@jwt_required()
def get_all_attendants():

    page = request.args.get('page', 1)
    per_page = request.args.get('per_page', 5)
    order = request.args.get('order_by', 'id_attendant')
    direction = request.args.get('dir', 'asc')
    name = request.args.get('name', '').title()

    if direction != 'asc' and direction != 'desc':
        direction = 'asc'

    options = {
        "asc": asc,
        "desc": desc
    }

    query_filter = and_((Attendants.nm_attendant.contains(name)))

    filtered_data = Attendants.query.filter(query_filter).order_by(options[direction](getattr(Attendants, order))).paginate(
        int(page), int(per_page), error_out=False).items

    """[comment]
        The code below is responsible for serialization the 'clinic' attribute  that is a 'Clinics' object, resulting only 'id_clinic' serialization 
    """
    response = list()
    for item in filtered_data:
        attendant_data = dict(item)
        clinic_data = attendant_data["clinic"]
        del attendant_data["clinic"]
        attendant_data["id_clinic"] = clinic_data.id_clinic
        response.append(attendant_data)

    return jsonify(response), 200

@only_role('ATD')
@jwt_required()
def get_attendant_by_id(id):

    filtered_data = Attendants.query.get(id)
    if filtered_data is None:
        return {"erro": "Recepcionista não encontrado"}

    """[comment]
        Understand the code below checking the explanation at comment in get_all_attendants function 
    """
    response = dict(filtered_data)
    clinic_data = response["clinic"]
    del response["clinic"]
    response["id_clinic"] = clinic_data.id_clinic

    return jsonify(response), 200
