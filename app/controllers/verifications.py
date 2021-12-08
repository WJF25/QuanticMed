from app.exc.excessoes import WrongKeyError
from app.exc.excessoes import NoExistingValueError
from app.exc.excessoes import NumericError, PasswordMinLengthError



def verify_keys(kwargs, option, method="post"):

    options = {
        "location": {'dt_start', 'dt_end', 'id_room', 'id_clinic', 'id_therapist'},
        "room": {'nm_room', 'id_specialty', 'ds_status'},
        "attendant": {'nm_attendant', 'nr_cpf', 'nr_telephone', 'nr_cellphone', 'ds_password', 'id_clinic', 'ds_email'},
        "customer": {'nm_customer', 'nr_cpf', 'nr_rg', 'nm_mother', 'nm_father', 'nr_healthcare', 'ds_address', 'nr_telephone', "nr_cellphone", 'ds_email', 'dt_birthdate'},
        "therapist": {'nm_therapist', 'nr_cpf', 'nr_crm', 'nm_user', 'ds_password', 'ds_specialties', 'nr_cellphone'}
    }

    keys = set(kwargs.keys())

    if method == "post":
        if len(keys) == 0:
            raise WrongKeyError({"Chaves Disponíveis": list(options[option])})
        elif not options[option].issubset(keys):
            error = list(keys - options[option] ) if list(keys - options[option] ) != [] else list(options[option] - keys)
            
            raise WrongKeyError({"Chaves_erradas":error, "Chaves Disponíveis":list(options[option])})
        elif not keys.issubset(options[option]):
            error = list(keys - options[option] )
            raise WrongKeyError({"Chaves_erradas":error, "Chaves Disponíveis":list(options[option])})
        
                    
    else:
        if len(keys) == 0:
            raise WrongKeyError({"Chaves Disponíveis": list(options[option])})

        if not keys.issubset(options[option]):
            error = list(keys - options[option])
            raise WrongKeyError({"Chaves_erradas":error, "Chaves Disponíveis":list(options[option])})
                   

        else:
            return True


def verify_none_values(value):
    
    if value == None:
        raise NoExistingValueError({"Erro": "Informação não existe no banco de dados"})


def is_numeric_data(*data):
    for item in data:
        if not item.isnumeric():
            raise NumericError(
                {"message": "The keys nr_cpf, nr_cellphone, nr_telephone should be numeric", "error": f"${item} isn't numeric"})


def password_min_length(data):
    if len(data) < 6:
        raise PasswordMinLengthError(
            {"error": "Password must be at least 6 characters"})
