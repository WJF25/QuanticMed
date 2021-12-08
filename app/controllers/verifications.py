from app.exc.excessoes import NumericError, PasswordMinLengthError, WrongKeyError
from ipdb import set_trace


def verify_keys(kwargs, option, method="post"):

    options = {
        "location": {'dt_start', 'dt_end', 'id_room', 'id_clinic', 'id_therapist'},
        "room": {'nm_room', 'id_specialty'},
        "attendant": {'nm_attendant', 'nr_cpf', 'nr_telephone', 'nr_cellphone', 'ds_password', 'id_clinic', 'ds_email'},
        "customer": {'nm_customer', 'nr_cpf', 'nr_rg', 'nm_mother', 'nm_father', 'nr_healthcare', 'ds_address', 'nr_telephone', "nr_cellphone", 'ds_email', 'dt_birthdate'},
        "therapist": {'nm_therapist', 'nr_cpf', 'nr_crm', 'nm_user', 'ds_password', 'ds_specialties'}
    }

    keys = set(kwargs.keys())

    if method == "post":
        if len(keys) == 0:
            raise WrongKeyError({"Chaves Disponíveis": list(options[option])})
        elif not options[option].issubset(keys):
            error = list(keys - options[option])

            raise WrongKeyError(
                {"Chaves_erradas": error, "Chaves Disponíveis": list(options[option])})

    else:

        if not keys.issubset(options[option]):
            error = list(keys - options[option])
            raise WrongKeyError(
                {"Chaves_erradas": error, "Chaves Disponíveis": list(options[option])})

        else:
            return True


def is_numeric_data(*data):
    for item in data:
        if not item.isnumeric():
            raise NumericError(
                {"message": "The keys nr_cpf, nr_cellphone, nr_telephone should be numeric", "error": f"${item} isn't numeric"})


def password_min_length(data):
    if len(data) < 6:
        raise PasswordMinLengthError(
            {"error": "Password must be at least 6 characters"})
