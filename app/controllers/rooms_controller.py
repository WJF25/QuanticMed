from flask import request, jsonify, current_app
from app.controllers.verifications import verify_keys, verify_none_values
from app.exc.excessoes import WrongKeyError, NoExistingValueError
from app.models.rooms_model import Rooms
from sqlalchemy.exc import DataError, IntegrityError
from sqlalchemy import desc, asc
from psycopg2.errors import ForeignKeyViolation, NotNullViolation
from app.models.sessions_model import Sessions
from app.models.therapists_model import Therapists
from app.models.locations_model import Locations
from flask_jwt_extended import jwt_required
from app.controllers.login_controller import only_role


@only_role('ATD')
@jwt_required()
def create_rooms():
    session = current_app.db.session

    try:
        data: dict = request.get_json()

        verify_keys(data, "room", "post")

        room = Rooms(**data)
        session.add(room)
        session.commit()
    except WrongKeyError as error:
        return jsonify({"Erro": error.value}), 400
    except DataError as data_error:
        return jsonify({"erro": "Id's são somente números, outros campos strings"}), 400
    except IntegrityError as int_error:
        if type(int_error.orig) == ForeignKeyViolation:
            return jsonify({"erro": "Chave(s) estrangeira(s) não existe(m)"}), 400
        if type(int_error.orig) == NotNullViolation:
            return jsonify({"erro": "Campo não pode ser nulo"}), 400

    return jsonify(room), 201


@only_role('ATD')
@jwt_required()
def delete_room(room_id):
    session = current_app.db.session

    room = Rooms.query.filter_by(id_room=room_id).first()

    if room is None:
        return jsonify({"erro": "Sala não existe"}), 404

    room_response = dict(room)
    session.delete(room)
    session.commit()

    return jsonify({}), 204


@only_role('ATD')
@jwt_required()
def update_room(room_id):
    session = current_app.db.session

    data: dict = request.get_json()

    try:
        verify_keys(data, "room", "patch")
        current_room = Rooms.query.filter_by(id_room=room_id).first()
        verify_none_values(current_room)

        updated_room = session.query(Rooms).filter_by(
            id_room=room_id).update(data)
        session.commit()
    except WrongKeyError as error:
        return jsonify({"Erro": error.value}), 400
    except DataError:
        return jsonify({"erro": "Id's são somente números, outros campos strings"}), 400
    except NoExistingValueError as error:
        return jsonify({"erro": error.value}), 404

    response = Rooms.query.get(room_id)

    return jsonify(response), 201


@only_role('ATD')
@jwt_required()
def get_rooms():
    session = current_app.db.session
    param: dict = dict(request.args)

    q_options = {
        "dsc": desc(getattr(Rooms, param.get('order_by', 'id_room'))),
        "asc": asc(getattr(Rooms, param.get('order_by', 'id_room')))
    }

    if param:
        if param.get('per_page'):
            ordered_rooms = session.query(Rooms)\
                .order_by(q_options.get(param.get("dir", "asc")))\
                .paginate(int(param.get('page', 1)), int(param.get('per_page', 30)), max_per_page=30).items

            return jsonify(ordered_rooms), 200

        ordered_rooms = session.query(Rooms)\
            .order_by(q_options.get(param.get("dir", "asc"))).all()

        return jsonify(ordered_rooms), 200

    rooms = session.query(Rooms).all()

    return jsonify(rooms), 200


@only_role('ATD')
@jwt_required()
def get_room_by_id(room_id):

    room = Rooms.query.filter_by(id_room=room_id).first()
    if room is None:
        return jsonify({"erro": "Sala não existe"}), 404

    return jsonify(room), 200


@only_role('ATD')
@jwt_required()
def get_room_by_status(room_status):

    param: dict = dict(request.args)

    q_options = {
        "dsc": desc(getattr(Rooms, param.get('order_by', 'id_room'))),
        "asc": asc(getattr(Rooms, param.get('order_by', 'id_room')))
    }

    room = Rooms.query.filter(Rooms.ds_status.ilike(
        '%' + room_status + '%')).order_by(q_options.get(param.get('dir', 'asc'))).all()
    if room is None:
        return jsonify({"erro": "Sala não existe"}), 404

    return jsonify(room), 200


@only_role('ATD')
@jwt_required()
def get_room_schedule(id_room):

    param: dict = dict(request.args)

    if param:
        room = Sessions.query.select_from(Sessions).join(Therapists).join(Locations).join(Rooms).filter(
            Rooms.id_room == id_room).filter(Sessions.ds_status == param.get("status_consulta", "agendado")).all()
        return jsonify(room), 200

    room = Sessions.query.select_from(Sessions).join(Therapists).join(Locations).join(Rooms).filter(
        Rooms.id_room == id_room).all()

    return jsonify(room), 200
