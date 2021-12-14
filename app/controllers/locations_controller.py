from flask import request, jsonify, current_app
from sqlalchemy.sql.elements import not_
from app.exc.excessoes import WrongKeyError, NoExistingValueError
from app.models.locations_model import Locations
from app.controllers.verifications import verify_keys, verify_none_values, verify_possiblle_dates
from psycopg2.errors import ForeignKeyViolation, UniqueViolation,NotNullViolation
from sqlalchemy.exc import IntegrityError, DataError
from datetime import datetime, timedelta
from sqlalchemy import desc, asc, between, and_, not_

from app.models.rooms_model import Rooms
from app.models.therapists_model import Therapists



def create_location():
    session = current_app.db.session

    try:
        data = request.get_json()
        verify_keys(data, "location", "post")    
        data['dt_end'] = datetime.strptime(data['dt_start'], "%d/%m/%Y %H:%M:%S") + timedelta(hours=int(data.get('dt_end', 1)[2:])) if "day" not in data.get('dt_end') else datetime.strptime(data['dt_start'], "%d/%m/%Y %H:%M:%S") + timedelta(days=int(data.get('dt_end', "day1")[3:]))
        query = Locations.query.where(Locations.id_room == data['id_room']).all()
        
        
        check = verify_possiblle_dates(query, data)

        if not check:
            return jsonify({"Erro": "período Não disponível para essa sala"}), 400

        location = Locations(**data)

        session.add(location)
        session.commit()
    except WrongKeyError as error:
        return jsonify({"Erro": error.value}), 400
    except (IntegrityError ) as int_error:
        if type(int_error.orig) == UniqueViolation:
            return jsonify({"error": "Locação Já existe"}), 409
        if type(int_error.orig) == NotNullViolation:
            return jsonify({"erro": "Campo não pode ser nulo"}), 400
        if type(int_error.orig) == ForeignKeyViolation:
            return jsonify({"erro": "Chave(s) estrangeira(s) não existe(m)"}), 400
    except DataError as data_error:
        return jsonify({"erro": "Id's são somente números, outros campos strings"}), 400
    
    response = dict(location)
    del response['clinic'], response['therapist']
    data = {"ds_status":"reservada"}
    response['room'] = dict(response['room'])
    response['room']['ds_status'] = data.get("ds_status", "null")
    Rooms.query.filter_by(id_room=response['room']['id_room']).update(data)
    session.commit()

    return jsonify(response), 201


def delete_location(location_id):
    session = current_app.db.session

    
    location = Locations.query.filter_by(id_location=location_id).first()
     
    if location is None:
        return jsonify({"erro": "Locação não existe"}), 404

    response_location = dict(location)
    session.delete(location)
    session.commit()
    del response_location['clinic'], response_location['therapist']

    data = {"ds_status":"livre"}
    response_location['room'] = dict(response_location['room'])
    response_location['room']['ds_status'] = data.get("ds_status", "null")
    Rooms.query.filter_by(id_room=response_location['room']['id_room']).update(data)
    session.commit()

    return jsonify({"Locação Excluída":response_location})


def update_location(location_id):
    session = current_app.db.session

    data:dict = request.get_json()

    try:
        
        verify_keys(data, "location", "patch")
        
        if data.get("dt_end", None) is not None and data.get("dt_start", None) is not None:
            data['dt_end'] = datetime.strptime(data['dt_start'], "%d/%m/%Y %H:%M:%S") + timedelta(hours=int(data.get('dt_end', 1)[2:])) if "day" not in data.get('dt_end') else datetime.strptime(data['dt_start'], "%d/%m/%Y %H:%M:%S")+ timedelta(days=int(data.get('dt_end', "day1")[3:]))
        elif data.get("dt_start", None) is None and data.get("dt_end", None) is not None:
            location_data = Locations.query.filter_by(id_location=location_id).first()
            to_update = dict(location_data)
            data['dt_end'] = to_update['dt_start'] + timedelta(hours=int(data.get('dt_end', 1)[2:])) if "day" not in data.get('dt_end') else to_update['dt_start']+ timedelta(days=int(data.get('dt_end', "day1")[3:]))
        elif data.get("dt_start", None) is not None and data.get("dt_end", None) is None:
            return{"erro": "Ao Atualizer a data de início, é preciso também alterar a data de término"}, 400

        location = Locations.query.filter_by(id_location=location_id).first()
        verify_none_values(location)
        
        Locations.query.filter_by(id_location=location_id).update(data)
        session.commit()        
    except WrongKeyError as error:
        return jsonify({"Erro": error.value}), 400
    except (IntegrityError ) as int_error:
        if type(int_error.orig) == UniqueViolation:
            return jsonify({"error": "Locação Já existe"}), 409
        if type(int_error.orig) == NotNullViolation:
            return jsonify({"erro": "Campo não pode ser nulo"}), 400
        if type(int_error.orig) == ForeignKeyViolation:
            return jsonify({"erro": "Chave(s) estrangeira(s) não existe(m)"}), 400
    except DataError as data_error:
        return jsonify({"erro": "Id's são somente números, outros campos strings"}), 400
    except  NoExistingValueError as error:
        return jsonify({"erro": error.value}), 404
    
    response = dict(location)
    del response['clinic'], response['therapist']

    return jsonify(response), 200


def get_locations():
    session = current_app.db.session

    param:dict = dict(request.args)    

    

    q_options = {
        "asc": asc(getattr(Locations, param.get('order_by', 'id_location'))),
        "dsc": desc(getattr(Locations, param.get('order_by', 'id_location'))),
        "filt_por":param.get('filt_por', 'id_location'),
        "filt_valor":param.get('filt_valor', "None"),
    }

    if param:
        try:
            date_locations = session.query(Locations)\
                .filter(q_options.get("filt_por") >= q_options.get("filt_valor"))\
                .order_by(q_options.get(param.get('dir', 'asc')))\
                .paginate( int(param.get('page',1)) ,int(param.get('per_page', 10)), max_per_page=20).items
        except AttributeError as error:
            return jsonify({"Erro": str(error)}), 400
        response = [dict(location) for location in date_locations]
        for location in response:
            location['room'] = dict(location['room'])
            location['clinic'] = dict(location['clinic'])
            location['therapist'] = dict(location['therapist'])
            del location['room']['id_room'], location['room']['specialty']
            del location['clinic']
            location['therapists'] = location['therapist']['nm_therapist']
            del location['therapist']
        return jsonify(response)


    locations = session.query(Locations).all()
    response = [dict(location) for location in locations]
    for location in response:
        location['room'] = dict(location['room'])
        location['clinic'] = dict(location['clinic'])
        location['therapist'] = dict(location['therapist'])
        del location['room']['id_room'], location['room']['specialty']
        del location['clinic']
        location['therapists'] = location['therapist']['nm_therapist']
        del location['therapist']
        

    return jsonify(response)


def get_locations_by_id(location_id):
    

    
    location = Locations.query.filter_by(id_location=location_id).first()

    if location is None:
        return jsonify({"erro": "Locação não existe"}), 404

    response:dict = dict(location)
    response['room'] = dict(response['room'])
    response['clinic'] = dict(response['clinic'])
    response['therapist'] = dict(response['therapist'])
    del response['room']['id_room'], response['room']['specialty']
    del response['clinic']
    response['therapists'] = response['therapist']['nm_therapist']
    del response['therapist']
    

    return jsonify(response)


def get_location_by_therapist(therapist_id):
    session = current_app.db.session
    location = session.query(Locations).join(Therapists)\
        .filter(Locations.id_therapist == therapist_id).all()
    response = [dict(location) for location in location]
    for location in response:
        location['room'] = dict(location['room'])
        location['clinic'] = dict(location['clinic'])
        location['therapist'] = dict(location['therapist'])
        del location['room']['specialty']
        del location['clinic']
        location['therapists'] = location['therapist']['nm_therapist']
        del location['therapist']
        
    return jsonify(response)