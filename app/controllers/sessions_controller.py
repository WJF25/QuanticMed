from flask import request, jsonify, current_app
from app.exc.excessoes import WrongKeyError, NoExistingValueError
from app.models.sessions_model import Sessions
from app.controllers.verifications import verify_keys
from psycopg2.errors import ForeignKeyViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import DataError

def create_appointment():
    session = current_app.db.session

    try:
        data = request.get_json()
        verify_keys(data, "session", "post")
        appointment = Sessions(**data)
        session.add(appointment)
        session.commit()
        response = dict(appointment)
    except WrongKeyError as error:
        return jsonify({"erro": error.value}), 400
    except DataError as data_error:
        return jsonify({"erro": "Id's são somente números, outros campos strings"}), 400
    except IntegrityError as int_error:
        if type(int_error.orig) == ForeignKeyViolation:
            return jsonify({"erro": "Chave(s) estrangeira(s) não existe(m)"}), 400

    return jsonify(response), 201

def update_appointment_by_id(session_id):
    session = current_app.db.session
    
    data = request.get_json()

    try:
        verify_keys(data, "session", "patch")
        appointment = Sessions.query.filter_by(id_session = session_id).first()
        if appointment is None:
            return jsonify({"erro": "Especialidade não existe"}), 404
        Sessions.query.filter_by(id_session = session_id).update(data)
        response = dict(appointment)
        session.commit()
    except WrongKeyError as error:
        return jsonify({"Erro": error.value}), 400
    except DataError as data_error:
        return jsonify({"erro": "Id's são somente números, outros campos strings"}), 400
    except NoExistingValueError as error:
        return jsonify({"erro": error.value}), 404
    except IntegrityError as int_error:
        if type(int_error.orig) == ForeignKeyViolation:
            return jsonify({"erro": "Chave(s) estrangeira(s) não existe(m)"}), 400

    return jsonify(response), 201

def delete_appointment(session_id):
    session = current_app.db.session

    appointment = Sessions.query.filter_by(id_session = session_id).first()
    if appointment is None:
        return jsonify({"erro": "Sessão não existe"}), 404
    session.delete(appointment)
    session.commit()

    return jsonify({}), 204

def get_appointment_by_id(session_id):
    session = current_app.db.session

    appointment = Sessions.query.filter_by(id_session = session_id).first()
    session.commit()
    if appointment is None:
        return jsonify({"erro": "Sessão não existe"}), 404

    return jsonify(appointment), 200

