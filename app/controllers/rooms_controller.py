from flask import request, jsonify, current_app
from app.controllers.verifications import verify_keys, verify_none_values
from app.exc.excessoes import WrongKeyError, NoExistingValueError
from app.models.rooms_model import Rooms
from sqlalchemy.exc import DataError
import sqlalchemy
import psycopg2



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

    return jsonify(room)


def delete_room(room_id):
    session = current_app.db.session
    

    room = Rooms.query.filter_by(id_room=room_id).first()
    romm_response = dict(room)
    
    if room is None:
        return jsonify({"erro": "Sala não existe"}), 404
    session.delete(room)
    session.commit()
    
    return jsonify({"Sala Deletada":romm_response})


def update_room(room_id):
    session = current_app.db.session

    data: dict = request.get_json()

    try:
        verify_keys(data, "room", "patch")
        current_room = Rooms.query.filter_by(id_room=room_id).first()
        verify_none_values(current_room)
        data["nm_room"] = data["nm_room"].title()
        updated_room = session.query(Rooms).filter_by(id_room=room_id).update(data)
        session.commit()
    except WrongKeyError as error:
        return jsonify({"Erro": error.value}), 400
    except DataError as data_error:
        return jsonify({"erro": "Id's são somente números, outros campos strings"}), 400
    except NoExistingValueError as error:
        return jsonify({"erro": error.value}), 404

    response = Rooms.query.get(room_id)

    return jsonify(response),201



def get_rooms():
    session = current_app.db.session
    param:dict = dict(request.args)
    
    
    if param:
        ordered_rooms = session.query(Rooms).order_by(getattr(Rooms, param['data'])).paginate(int(param.get('page',1)),int(param.get('per_page',10)), max_per_page=20).items
        response = [dict(room) for room in ordered_rooms]
        return jsonify(response)


    rooms = session.query(Rooms).paginate(int(param.get('page',1)),int(param.get('per_page',10)), max_per_page=20).items
    response = [dict(room) for room in rooms]

    return jsonify(response)

    



def get_room_by_id(room_id):
    session = current_app.db.session

    room = Rooms.query.filter_by(id_room=room_id).first()
    if room is None:
        return jsonify({"erro": "Sala não existe"}), 404

    return jsonify(room)


def get_room_by_status(room_status):
    session = current_app.db.session

    room = Rooms.query.filter(Rooms.ds_status.ilike('%' + room_status + '%')).all()
    if room is None:
        return jsonify({"erro": "Sala não existe"}), 404

    return jsonify(room)