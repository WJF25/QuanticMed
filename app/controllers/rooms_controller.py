from flask import request, jsonify, current_app
from app.models.rooms_model import Rooms
import sqlalchemy 
import psycopg2



def create_rooms():    
    session = current_app.db.session
    data = request.get_json()
    room = Rooms(**data)
    session.add(room)
    session.commit()

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
