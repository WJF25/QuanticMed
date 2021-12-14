from flask import request, jsonify, current_app
from psycopg2.errorcodes import UNIQUE_VIOLATION, STRING_DATA_RIGHT_TRUNCATION
from psycopg2.errors import NotNullViolation
from sqlalchemy import and_, asc, desc
from sqlalchemy.exc import IntegrityError, DataError
from app.exc.excessoes import NumericError, WrongKeyError, EmailError
from app.models.customers_model import Customers
from app.models.sessions_model import Sessions
from app.models.therapists_model import Therapists
from app.controllers.verifications import verify_keys
from app.models.specialties_model import Specialties
from sqlalchemy import asc, desc, and_
from flask_jwt_extended import jwt_required
from app.controllers.login_controller import only_role

@only_role('ATD')
@jwt_required()
def create_therapist():
    session = current_app.db.session

    try:
        data = request.get_json()
        verify_keys(data, "therapist", "patch")

        specialties_data = data.pop('ds_specialties')

        inserted_data = Therapists(**data)

        for specialty in specialties_data:
            filtered_data = Specialties.query.filter_by(
                nm_specialty=specialty['nm_specialty']).first()
            if not filtered_data:
                new_specialty = Specialties(**specialty)
                inserted_data.specialties.append(new_specialty)
            else:
                inserted_data.specialties.append(filtered_data)

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
            return {"error": "Cpf, crm, email ou username já cadastrados"}, 409
        if type(e.orig) == NotNullViolation:
            return jsonify({"erro": "Campo não pode ser nulo"}), 400
    except NumericError as error:
        return jsonify(error.value), 400
    except WrongKeyError as error:
        return jsonify({"Error": error.value}), 400

@only_role('ATD')
@jwt_required()
def update_therapist(id):
    session = current_app.db.session

    data = request.get_json()

    try:
        verify_keys(data, "therapist", "patch")

        filtered_data = Therapists.query.get(id)
        if filtered_data is None:
            return {"error": "Terapeuta não encontrado"}

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
            return {"error": "Cpf, crm, email ou username já cadastrados"}, 409
        if type(e.orig) == NotNullViolation:
            return jsonify({"erro": "Campo não pode ser nulo"}), 400
    except NumericError as error:
        return jsonify(error.value), 400
    except WrongKeyError as error:
        return jsonify({"Error": error.value}), 400

    return jsonify(filtered_data), 200


@only_role('ATD')
@jwt_required()
def delete_therapist(id):
    session = current_app.db.session

    filtered_data = Therapists.query.get(id)
    if filtered_data is None:
        return {"error": "Terapeuta não encontrado"}

    session.delete(filtered_data)
    session.commit()

    return '', 204

@only_role('ATD')
@jwt_required()
def get_all_therapists():

    page = request.args.get('page', 1)
    per_page = request.args.get('per_page', 5)
    order = request.args.get('order_by', 'id_therapist')
    direction = request.args.get('dir', 'asc')
    name = request.args.get('name', '').title()
    status = request.args.get('status', '')

    if direction != 'asc' and direction != 'desc':

        direction = 'asc'

    options = {
        "asc": asc,
        "desc": desc
    }

    query_filter = and_((Therapists.nm_therapist.contains(
        name)), (Therapists.ds_status.contains(status)))

    filtered_data = Therapists.query.filter(query_filter).order_by(options[direction](getattr(Therapists, order))).paginate(
        int(page), int(per_page), error_out=False).items

    response = list()
    for item in filtered_data:
        therapist_data = dict(item)
        response.append(therapist_data)

    return jsonify(response), 200

@only_role('ATD')
@jwt_required()
def get_therapist_by_id(id):
    filtered_data = Therapists.query.get(id)
    if filtered_data is None:
        return {"erro": "Terapeuta não encontrado"}

    return jsonify(filtered_data), 200


@jwt_required()
def get_costumer_by_therapist(therapist_id):

    therapist = Customers.query.select_from(Customers).join(Sessions).join(
        Therapists).filter_by(id_therapist=therapist_id).all()

    if len(therapist) == 0:
        return {"erro": "Este terapeuta não possui nenhum cliente"}

    return jsonify(therapist), 200


def get_therapist_schedule(id):
    page = request.args.get('page', 1)
    per_page = request.args.get('per_page', 20)
    status = request.args.get('status', '')
    order = request.args.get('order_by', 'dt_start')
    direction = request.args.get('dir', 'desc')

    if direction != 'asc' and direction != 'desc':
        direction = 'asc'

    options = {
        'asc': asc,
        'desc': desc
    }

    query_filter = (and_((Sessions.id_therapist == id),
                    (Sessions.ds_status.contains(status))))

    filtered_data = Sessions.query.select_from(
        Sessions).join(Therapists).filter(query_filter).order_by(options[direction](getattr(Sessions, order))).paginate(int(page), int(per_page), error_out=False).items

    return jsonify(filtered_data), 200
