from flask import request, jsonify, current_app
from app.exc.excessoes import WrongKeyError, NoExistingValueError
from app.models.locations_model import Locations
from app.controllers.verifications import verify_keys, verify_none_values
from psycopg2.errors import UniqueViolation,NotNullViolation
from sqlalchemy.exc import IntegrityError, DataError
from datetime import datetime, timedelta
import sqlalchemy 



def create_location():
    session = current_app.db.session

    try:
        data = request.get_json()
        verify_keys(data, "location", "post")
        data['dt_start'] = datetime.now()
        data['dt_end'] = datetime.now() + timedelta(hours=int(data.get('dt_end', 1)[2:])) if "day" not in data.get('dt_end') else datetime.now() + timedelta(days=int(data.get('dt_end', "day1")[3:]))

        location = Locations(**data)

        session.add(location)
        session.commit()
        

        response = dict(location)
    except WrongKeyError as error:
        return jsonify({"Erro": error.value}), 400
    except (IntegrityError ) as int_error:
        if type(int_error.orig) == UniqueViolation:
            return jsonify({"error": "Locação Já existe"}), 409
        if type(int_error.orig) == NotNullViolation:
            return jsonify({"erro": "Campo não pode ser nulo"}), 400
    except DataError as data_error:
        return jsonify({"erro": "Id's são somente números, outros campos strings"}), 400

    del response['clinic'], response['therapist']

    return jsonify(response), 201


def delete_location(location_id):
    session = current_app.db.session

    
    location = Locations.query.filter_by(id_location=location_id).first()
    response_location = dict(location)
    if location is None:
        return jsonify({"erro": "Locação não existe"}), 404
    session.delete(location)
    session.commit()

    return jsonify({"Locação Excluída":response_location})


def update_location(location_id):
    session = current_app.db.session

    data = request.get_json()

    try:
        location = Locations.query.filter_by(id_location=location_id).first()
        verify_none_values(location)
    except  NoExistingValueError as error:
        return jsonify({"erro": error.value}), 404
    

    try:
        
        verify_keys(data, "location", "patch")
        
        location.update(**data)
        session.commit()
        response = dict(location)
    except WrongKeyError as error:
        return jsonify({"Erro": error.value}), 400
    except (IntegrityError ) as int_error:
        if type(int_error.orig) == UniqueViolation:
            return jsonify({"error": "Locação Já existe"}), 409
        if type(int_error.orig) == NotNullViolation:
            return jsonify({"erro": "Campo não pode ser nulo"}), 400
    except DataError as data_error:
        return jsonify({"erro": "Id's são somente números, outros campos strings"}), 400

    del response['clinic'], response['therapist']

    return jsonify(response), 200
