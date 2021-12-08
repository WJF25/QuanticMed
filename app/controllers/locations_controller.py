from flask import request, jsonify, current_app
from app.models.locations_model import Locations
import psycopg2
import sqlalchemy 



def create_location():
    session = current_app.db.session

    data = request.get_json()
    location = Locations(**data)
    session.add(location)
    session.commit()

    response = dict(data)
    del response['clinic'], response['therapists']
    
    
    
    return jsonify(location)

