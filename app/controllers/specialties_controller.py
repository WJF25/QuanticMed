from flask import request, jsonify, current_app
from app.exc.excessoes import NullObject, WrongKeyError
from app.models.specialties_model import Specialties
from app.controllers.verifications import verify_keys, delete_invalid_keys
from psycopg2.errors import UniqueViolation,NotNullViolation
from sqlalchemy.exc import IntegrityError

def create_specialty():
    session = current_app.db.session

    try:
        data = request.get_json()
        delete_invalid_keys("specialties", data)
        verify_keys(data, "specialties", "post")
        specialty = Specialties(**data)
        session.add(specialty)
        session.commit()
        response = dict(specialty)

    except NullObject:
        return jsonify({"erro": "Objeto não pode ser nulo ou possui chaves erradas"}), 400
    except WrongKeyError as error:
        return jsonify({"erro": error.value}), 400
    except IntegrityError as int_error:
        if type(int_error.orig) == UniqueViolation:
            return jsonify({"erro": "Especialidade já existe"}), 409
        if type(int_error.orig) == NotNullViolation:
            return jsonify({"erro: Campo não pode ser vazio"}), 400
        
    return jsonify(response), 201

def update_specialty_by_id(specialty_id):
    session = current_app.db.session

    try:
        data = request.get_json()
        delete_invalid_keys("specialties", data)
        specialty = Specialties.query.filter_by(id_specialty = specialty_id).first()
        if specialty is None:
            return jsonify({"erro": "Especialidade não existe"}), 404
        Specialties.query.filter_by(id_specialty = specialty_id).update(data)
        response = dict(specialty)
        session.commit()
    except NullObject:
        return jsonify({"erro": "Objeto não pode ser nulo ou possui chaves erradas"}), 400
    except IntegrityError as int_error:
        if type(int_error.orig) == UniqueViolation:
            return jsonify({"erro": "Especialidade já existe"}), 409

    return jsonify(response), 201

def delete_specialty(specialty_id):
    session = current_app.db.session

    specialty = Specialties.query.filter_by(id_specialty = specialty_id).first()
    if specialty is None:
        return jsonify({"erro": "Especialidade não existe"}), 404
    response = dict(specialty)
    session.delete(specialty)
    session.commit()

    return jsonify({"Especialidade Excluída": response}), 200