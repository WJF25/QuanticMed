from flask import request, jsonify, current_app
import sqlalchemy
import psycopg2
from sqlalchemy import and_, or_
from app.models.attendants_model import Attendants
from sqlalchemy.exc import IntegrityError
from psycopg2.errorcodes import UNIQUE_VIOLATION
from app.controllers.verifications import verify_keys, is_numeric_data
from app.exc.excessoes import NumericError, PasswordMinLengthError, WrongKeyError
from ipdb import set_trace


def create_attendant():

    session = current_app.db.session

    try:
        data = request.get_json()

        verify_keys(data, "attendant", "post")
        is_numeric_data(
            data['nr_cpf'], data['nr_cellphone'], data['nr_telephone'])

        inserted_data = Attendants(**data)

        session.add(inserted_data)
        session.commit()

        return jsonify(inserted_data), 201

    except WrongKeyError as error:
        return jsonify({"Error": error.value}), 400
    except NumericError as error:
        return jsonify(error.value), 400
    except PasswordMinLengthError as error:
        return jsonify(error.value), 400
    except IntegrityError as e:
        if e.orig.pgcode == UNIQUE_VIOLATION:
            return {"error": "task name already exists"}, 409
        return str(e), 404


# TODO: INTEGRAR COM AS CLINICAS DEVIDO A FK
# FIXME: VALOR DEFAULT DO creating_time
