from flask import request, jsonify, current_app
from psycopg2.errorcodes import UNIQUE_VIOLATION
import sqlalchemy
import psycopg2
from sqlalchemy.exc import IntegrityError
from app.exc.excessoes import NumericError, PasswordMinLengthError, WrongKeyError
from app.models.therapists_model import Therapists
from app.controllers.verifications import is_numeric_data, verify_keys, password_min_length
from app.models.specialties_model import Specialties


def create_therapist():
    session = current_app.db.session

    try:
        data = request.get_json()
        verify_keys(data, "therapist", "patch")

        specialties_data = data.pop('ds_specialties')

        is_numeric_data(
            data['nr_cpf'])
        password_min_length(data['ds_password'])

        inserted_data = Therapists(**data)

        for specialty in specialties_data:
            filtered_data = Specialties.query.filter_by(
                nm_specialty=specialty['nm_specialty']).first()
            if not filtered_data:
                new_specialty = Specialties(**specialty)
                inserted_data.specialties.append(new_specialty)
            else:
                inserted_data.specialties.append(filtered_data)

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
            return {"error": "Therapist name already exists"}, 409
        return str(e), 404
