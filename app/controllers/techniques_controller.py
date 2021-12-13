from flask import request, jsonify, current_app
from app.exc.excessoes import WrongKeyError, NoExistingValueError
from app.controllers.verifications import verify_keys
from app.models.techniques_model import Techniques
from app.models.customers_model import Customers
from psycopg2.errors import ForeignKeyViolation,NotNullViolation
from sqlalchemy.exc import IntegrityError

def create_technique():
    session = current_app.db.session

    try:
        data = request.get_json()
        verify_keys(data, "technique", "post")
        customer = session.query(Customers).filter_by(nm_customer = data["nm_customer"]).first()
        if customer == None:
            return jsonify({"erro": "Usuário não encontrado"}), 404
        customer_record = customer.record
        data['id_customer_record'] = customer_record.id_customer_record
        del data['nm_customer']
        technique = Techniques(**data)
        session.add(technique)
        session.commit()
        response = dict(technique)

    except WrongKeyError as error:
        return jsonify({"erro": error.value}), 400
    except (IntegrityError ) as int_error:
        if type(int_error.orig) == NotNullViolation:
            return jsonify({"erro": "Campo não pode ser nulo"}), 400
        if type(int_error.orig) == ForeignKeyViolation:
            return jsonify({"erro": "Chave(s) estrangeira(s) não existe(m)"}), 400
    
    return jsonify(response), 201

def update_technique_by_id(technique_id):
    session = current_app.db.session
    
    data = request.get_json()

    try:
        verify_keys(data, "technique", "patch")
        technique = Techniques.query.filter_by(id_technique = technique_id).first()
        if technique is None:
            return jsonify({"erro": "Tecnica não existe"}), 404
        if data.get('nm_customer') != None:
            customer = session.query(Customers).filter_by(nm_customer = data["nm_customer"]).first()
            if customer == None:
                return jsonify({"erro": "Usuário não encontrado"}), 404
            customer_record = customer.record
            data['id_customer_record'] = customer_record.id_customer_record
            del data['nm_customer']
        Techniques.query.filter_by(id_technique = technique_id).update(data)
        session.commit()
    except WrongKeyError as error:
        return jsonify({"erro": error.value}), 400
    except NoExistingValueError as error:
        return jsonify({"erro": error.value}), 404
    except IntegrityError as int_error:
        if type(int_error.orig) == NotNullViolation:
            return jsonify({"erro: Campo não pode ser vazio"}), 400
        if type(int_error.orig) == ForeignKeyViolation:
            return jsonify({"erro": "Chave(s) estrangeira(s) não existe(m)"}), 400

    response = Techniques.query.get(technique_id)
    session.commit()

    return jsonify(response), 201



def delete_technique(technique_id):
    session = current_app.db.session

    technique = Techniques.query.filter_by(id_technique = technique_id).first()
    if technique is None:
        return jsonify({"erro": "Tecnica não existe"}), 404
    response = dict(technique)
    session.delete(technique)
    session.commit()

    return jsonify({"Tecnica Excluída": response}), 200

def get_techniques():
    session = current_app.db.session
    param:dict = dict(request.args)
    
    
    if param:
        ordered_techniques = session.query(Techniques).paginate(int(param.get('page',1)),int(param.get('per_page',10)), max_per_page=20).items
        response = [dict(technique) for technique in ordered_techniques]
        return jsonify(response)


    techniques = session.query(Techniques).paginate(int(param.get('page',1)),int(param.get('per_page',10)), max_per_page=20).items
    response = [dict(technique) for technique in techniques]

    return jsonify(response), 200

def get_techniques_by_id(technique_id):
    session = current_app.db.session

    technique = Techniques.query.filter_by(id_technique = technique_id).first()
    if technique is None:
        return jsonify({"erro": "Tecnica não existe"}), 404
    response = dict(technique)
    session.commit()

    return jsonify(response), 200


