from flask import request, jsonify, current_app
from app.exc.excessoes import WrongKeyError, NoExistingValueError
from app.models.specialties_model import Specialties
from app.controllers.verifications import verify_keys, verify_none_values
from psycopg2.errors import UniqueViolation,NotNullViolation
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required
from app.controllers.login_controller import only_role

@only_role('ATD')
@jwt_required()
def create_specialty():
    session = current_app.db.session

    try:
        data = request.get_json()
        verify_keys(data, "specialty", "post")
        specialty = Specialties(**data)
        session.add(specialty)
        session.commit()
        response = dict(specialty)

    except WrongKeyError as error:
        return jsonify({"erro": error.value}), 400
    except IntegrityError as int_error:
        if type(int_error.orig) == UniqueViolation:
            return jsonify({"erro": "Especialidade já existe"}), 409
        if type(int_error.orig) == NotNullViolation:
            return jsonify({"erro": "Campo não pode ser vazio"}), 400
        
    return jsonify(response), 201

@only_role('ATD')
@jwt_required()
def update_specialty_by_id(specialty_id):
    session = current_app.db.session
    
    data = request.get_json()

    try:
        verify_keys(data, "specialty", "patch")
        specialty = Specialties.query.filter_by(id_specialty = specialty_id).first()
        if specialty is None:
            return jsonify({"erro": "Especialidade não existe"}), 404
        verify_none_values(specialty)
        Specialties.query.filter_by(id_specialty = specialty_id).update(data)
        session.commit()
    except WrongKeyError as error:
        return jsonify({"erro": error.value}), 400
    except NoExistingValueError as error:
        return jsonify({"erro": error.value}), 404
    except IntegrityError as int_error:
        if type(int_error.orig) == UniqueViolation:
            return jsonify({"erro": "Especialidade já existe"}), 409
        if type(int_error.orig) == NotNullViolation:
            return jsonify({"erro": "Campo não pode ser vazio"}), 400

    response = Specialties.query.get(specialty_id)
    session.commit()

    return jsonify(response), 201

@only_role('ATD')
@jwt_required()
def delete_specialty(specialty_id):
    session = current_app.db.session

    specialty = Specialties.query.filter_by(id_specialty = specialty_id).first()
    if specialty is None:
        return jsonify({"erro": "Especialidade não existe"}), 404
    session.delete(specialty)
    session.commit()

    return jsonify({}), 204

@only_role('ATD')
@jwt_required()
def get_specialties():
    session = current_app.db.session
    param:dict = dict(request.args)
    
    
    if param:
        ordered_specialties = session.query(Specialties).paginate(int(param.get('page',1)),int(param.get('per_page',40)), max_per_page=20).items
        response = [dict(specialty) for specialty in ordered_specialties]
        return jsonify(response), 200


    specialties = session.query(Specialties).paginate(int(param.get('page',1)),int(param.get('per_page',40)), max_per_page=20).items
    response = [dict(specialty) for specialty in specialties]

    return jsonify(response), 200

