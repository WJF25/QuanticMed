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
