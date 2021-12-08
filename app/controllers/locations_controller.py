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

    response = dict(location)
     
    del response['clinic'], response['therapist']
        
    
    
    return jsonify(response)


def delete_location(location_id):
    session = current_app.db.session

    
    location = Locations.query.filter_by(id_location=location_id).first()
    response_location = dict(location)
    session.delete(location)
    session.commit()

    return jsonify({"Locação Excluída":response_location})

