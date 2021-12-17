from flask import request, jsonify, current_app
from psycopg2.errorcodes import STRING_DATA_RIGHT_TRUNCATION
from app.exc.excessoes import WrongKeyError, NoExistingValueError
from app.controllers.verifications import verify_keys
from app.models.techniques_model import Techniques
from app.models.customers_model import Customers
from psycopg2.errors import ForeignKeyViolation, NotNullViolation
from sqlalchemy.exc import IntegrityError, DataError
from flask_jwt_extended import jwt_required
from app.controllers.login_controller import only_role
from sqlalchemy.orm.exc import StaleDataError


@only_role('TRP')
@jwt_required()
def create_technique():
    session = current_app.db.session

    try:
        data = request.get_json()
        verify_keys(data, "technique", "post")
        technique = Techniques(**data)
        session.add(technique)
        session.commit()
        response = dict(technique)

    except DataError as e:
        if e.orig.pgcode == STRING_DATA_RIGHT_TRUNCATION:
            return {"error": "Valor mais longo que o permitido"}, 400
    except WrongKeyError as error:
        return jsonify({"erro": error.value}), 400
    except (IntegrityError) as int_error:
        if type(int_error.orig) == NotNullViolation:
            return jsonify({"erro": "Campo não pode ser nulo"}), 400
        if type(int_error.orig) == ForeignKeyViolation:
            return jsonify({"erro": "Chave(s) estrangeira(s) não existe(m)"}), 400
    except ValueError:
        return jsonify({"erro": "Formato de data errado. Formato válido: %m/%d/%Y"}), 400

    return jsonify(response), 201


@only_role('TRP')
@jwt_required()
def update_technique_by_id(technique_id):
    session = current_app.db.session

    data = request.get_json()

    try:
        verify_keys(data, "technique", "patch")
        technique = Techniques.query.filter_by(
            id_technique=technique_id).first()
        if technique is None:
            return jsonify({"erro": "Tecnica não existe"}), 404
        Techniques.query.filter_by(id_technique=technique_id).update(data)
        session.commit()
    except DataError as e:
        if e.orig.pgcode == STRING_DATA_RIGHT_TRUNCATION:
            return {"error": "Valor mais longo que o permitido"}, 400
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


@only_role('TRP')
@jwt_required()
def delete_technique(technique_id):
    session = current_app.db.session
    try:
        technique = Techniques.query.filter_by(
            id_technique=technique_id).first()
        if technique is None:
            return jsonify({"erro": "Tecnica não existe"}), 404
        session.delete(technique)
        session.commit()
    except StaleDataError:
        return jsonify({"Error": "Esta técnica é chave estrageira de outra entidade."}), 405

    return jsonify({}), 204


@only_role('TRP')
@jwt_required()
def get_techniques():
    session = current_app.db.session
    param: dict = dict(request.args)

    if param:
        ordered_techniques = session.query(Techniques).paginate(
            int(param.get('page', 1)), int(param.get('per_page', 10)), max_per_page=20).items
        response = [dict(technique) for technique in ordered_techniques]
        return jsonify(response), 200

    techniques = session.query(Techniques).all()
    response = [dict(technique) for technique in techniques]

    return jsonify(response), 200


@only_role('TRP')
@jwt_required()
def get_techniques_by_id(technique_id):
    session = current_app.db.session

    technique = Techniques.query.filter_by(id_technique=technique_id).first()
    if technique is None:
        return jsonify({"erro": "Tecnica não existe"}), 404
    response = dict(technique)
    session.commit()

    return jsonify(response), 200
