from flask import request, jsonify, current_app
from app.exc.excessoes import WrongKeyError, NoExistingValueError
from app.exc.sessions_errors import SessionDateAlreadyInUse
from app.models.customers_model import Customers
from app.models.sessions_model import Sessions
from app.models.therapists_model import Therapists
from app.services.schedule_emails import get_appointments_emails
from app.controllers.verifications import verify_keys
from psycopg2.errors import ForeignKeyViolation
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import DataError
from sqlalchemy import and_, or_
import datetime
from smtplib import SMTPAuthenticationError
from flask_jwt_extended import jwt_required
from app.controllers.login_controller import only_role
from sqlalchemy.orm.exc import StaleDataError


@only_role('ATD')
@jwt_required()
def create_appointment():
    data = request.get_json()
    session = current_app.db.session
    appointments = session.query(Sessions).filter(and_(
        Sessions.id_therapist == data["id_therapist"], Sessions.ds_status == "agendado")).all()
    dict_appoint = [dict(appointment) for appointment in appointments]
    try:
        # date_start = data["dt_start"]
        # date_end = data["dt_end"]
        # for i in dict_appoint:
        #     d1 = datetime.datetime.strptime(
        #         str(date_start), "%d/%m/%Y %H:%M:%S")
        #     d2 = datetime.datetime.strptime(date_end, "%d/%m/%Y %H:%M:%S")
        #     d3 = datetime.datetime.strptime(
        #         str(i["dt_start"]), "%Y-%m-%d %H:%M:%S"
        #     )
        #     d4 = datetime.datetime.strptime(
        #         str(i["dt_end"]), "%Y-%m-%d %H:%M:%S"
        #     )
        #     if d1 >= d3 and d2 <= d4:
        #         raise SessionDateAlreadyInUse("data já está sendo usada")
        #     if d1 >= d3 and d1 <= d4 or d2 > d3 and d2 <= d4:
        #         raise SessionDateAlreadyInUse("data já está sendo usada")
        #     if d1 <= d3 and d2 >= d4:
        #         raise SessionDateAlreadyInUse("data já está sendo usada")
        verify_keys(data, "session", "post")
        appointment = Sessions(**data)
        session.add(appointment)
        session.commit()
        response = dict(appointment)
        # get_appointments_emails(response.get("id_session"))
    except WrongKeyError as error:
        return jsonify({"erro": error.value}), 400
    except DataError as e:
        return jsonify({"erro":str(e)}), 400
    except IntegrityError as int_error:
        if type(int_error.orig) == ForeignKeyViolation:
            return jsonify({"erro": "Chave(s) estrangeira(s) não existe(m)"}), 400
    except SessionDateAlreadyInUse as Error:
        return {"erro": Error.value}, 409
    except SMTPAuthenticationError:
        return jsonify({"erro": "Email ou senha não conferem"}), 400

    return jsonify(response), 201


@jwt_required()
def update_appointment_by_id(session_id):
    session = current_app.db.session

    data = request.get_json()

    try:
        verify_keys(data, "session", "patch")
        appointment = Sessions.query.filter_by(id_session=session_id).first()
        if appointment is None:
            return jsonify({"erro": "Especialidade não existe"}), 404
        Sessions.query.filter_by(id_session=session_id).update(data)
        response = dict(appointment)
        session.commit()
    except WrongKeyError as error:
        return jsonify({"Erro": error.value}), 400
    except DataError:
        return jsonify({"erro": "Id's são somente números, outros campos strings"}), 400
    except NoExistingValueError as error:
        return jsonify({"erro": error.value}), 404
    except IntegrityError as int_error:
        if type(int_error.orig) == ForeignKeyViolation:
            return jsonify({"erro": "Chave(s) estrangeira(s) não existe(m)"}), 400

    return jsonify(response), 201


@only_role('ATD')
@jwt_required()
def delete_appointment(session_id):
    session = current_app.db.session

    try:
        appointment = Sessions.query.filter_by(id_session=session_id).first()
        if appointment is None:
            return jsonify({"erro": "Sessão não existe"}), 404
        session.delete(appointment)
        session.commit()
    except StaleDataError:
        return jsonify({"Error": "Esta sessão é chave estrageira de outra entidade."}), 405

    return jsonify({}), 204


@jwt_required()
def get_appointment_by_id(session_id):
    session = current_app.db.session

    appointment = Sessions.query.filter_by(id_session=session_id).first()
    session.commit()
    if appointment is None:
        return jsonify({"erro": "Sessão não existe"}), 404

    return jsonify(appointment), 200


@jwt_required()
def get_all_appointments():
    session = current_app.db.session
    status = request.args.get('status', "")

    query_filter = and_((Sessions.ds_status.contains(status)))
    appointments = Sessions.query.filter(query_filter).all()
    session.commit()

    response = [dict(appointment) for appointment in appointments]
    for appointment in response:
        customer = session.query(Customers).filter_by(
            id_customer=appointment['id_customer']).first()
        therapist = session.query(Therapists).filter_by(
            id_therapist=appointment['id_therapist']).first()
        appointment['customer'] = customer
        appointment['therapist'] = therapist
    return jsonify(response), 200
