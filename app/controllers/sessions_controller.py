from flask import request, jsonify, current_app
from werkzeug.wrappers import response
from app.exc.excessoes import NullObject, WrongKeyError
from app.models.sessions_model import Sessions
from app.controllers.verifications import verify_keys, delete_invalid_keys
from psycopg2.errors import UniqueViolation,NotNullViolation
from sqlalchemy.exc import IntegrityError

def create_appointment():
    session = current_app.db.session
    try:
        data = request.get_json()
        delete_invalid_keys("appointment", data)
        appointment = Sessions(**data)
        session.add(appointment)
        session.commit()
        response = dict(appointment)
    except WrongKeyError as error:
        return jsonify({"erro": error.value}), 400
    except NullObject:
        return jsonify({"erro": "Objeto não pode ser nulo ou possui chaves erradas"}), 400
    except IntegrityError as int_error:
        if type(int_error.orig) == NotNullViolation:
            return jsonify({"erro: Campo não pode ser vazio"}), 400 

    return jsonify(response), 201

def update_appointment_by_id(session_id):
    session = current_app.db.session

    try:
        data = request.get_json()
        delete_invalid_keys("appointment", data)
        appointment = Sessions.query.filter_by(id_session = session_id).first()
        if appointment is None:
            return jsonify({"erro": "Especialidade não existe"}), 404
        Sessions.query.filter_by(id_session = session_id).update(data)
        response = dict(appointment)
        session.commit()
    except NullObject:
        return jsonify({"erro": "Objeto não pode ser nulo ou possui chaves erradas"}), 400
    except IntegrityError as int_error:
        if type(int_error.orig) == UniqueViolation:
            return jsonify({"erro": "Sessão já existe"}), 409

    return jsonify(response), 201

def delete_appointment(session_id):
    session = current_app.db.session

    appointment = Sessions.query.filter_by(id_session = session_id).first()
    if appointment is None:
        return jsonify({"erro": "Sessão não existe"}), 404
    response = dict(appointment)
    session.delete(appointment)
    session.commit()

    return jsonify({"Especialidade Excluída": response}), 200

