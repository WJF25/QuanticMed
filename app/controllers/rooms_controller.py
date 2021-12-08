from flask import request, jsonify, current_app
from app.controllers.verifications import verify_keys
from app.exc.excessoes import WrongKeyError
from app.models.rooms_model import Rooms
from sqlalchemy.exc import DataError
import sqlalchemy 
import psycopg2



def create_rooms():    
    session = current_app.db.session

    try:
        data: dict = request.get_json()
        
        verify_keys(data, "room", "post")

        data["nm_room"] = data["nm_room"].title()
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

    current_room = Rooms.query.filter_by(id_room=room_id).first()
    if current_room is None:
        return jsonify({"erro": "Sala não existe"}), 404

    try:
        verify_keys(data, "room", "patch")
        data["nm_room"] = data["nm_room"].title()
        updated_room = session.query(Rooms).filter_by(id_room=room_id).update(data)
        session.commit()
    except WrongKeyError as error:
        return jsonify({"Erro": error.value}), 400
    except DataError as data_error:
        return jsonify({"erro": "Id's são somente números, outros campos strings"}), 400

    response = Rooms.query.get(room_id)

    return jsonify(response),201
