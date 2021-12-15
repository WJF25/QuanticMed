from flask import request, current_app, jsonify
from flask_jwt_extended.utils import get_jwt
from flask_jwt_extended.view_decorators import verify_jwt_in_request
from app.models.therapists_model import Therapists
from app.models.attendants_model import Attendants
from app.controllers.verifications import verify_keys
from app.exc.excessoes import WrongKeyError
from flask_jwt_extended import create_access_token
from functools import wraps

flags_dict = {
    'TRP': 'Terapeutas',
    'ATD': 'Atendentes'
    }

def login():
    session = current_app.db.session

    data = request.json
    try:
        verify_keys(data, "login", "post")
        therapist: Therapists = session.query(Therapists).filter_by(nr_cpf=data['nr_cpf']).first()
        attendant: Attendants = session.query(Attendants).filter_by(nr_cpf=data['nr_cpf']).first()

        if therapist == None and attendant  == None:
            return jsonify({"erro": "Não existe usuário com este CPF"}), 404

        if therapist != None:
            if therapist.check_password(data['ds_password']):
                access_token = create_access_token(therapist)
                return jsonify({"token":access_token}), 200
            else:
                return jsonify({"erro":"CPF e password não combinam"}), 401
        
        if attendant != None:
            if attendant.check_password(data['ds_password']):
                access_token = create_access_token(attendant)
                return jsonify({"token":access_token}), 200
            else:
                return jsonify({"erro":"CPF e password não combinam"}), 401
    except WrongKeyError as error:
        return jsonify({"erro": error.value}), 400

def only_role(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if role == claims['sub']['fl_admin']:
                return fn(*args, **kwargs)
            else:
                return jsonify({"erro":f"Acesso não autorizado. Esta rota está restrita para {flags_dict[role]}."}), 403
        return decorator
    return wrapper