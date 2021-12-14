from app.exc.excessoes import WrongKeyError
from app.exc.excessoes import NoExistingValueError
from app.exc.excessoes import NumericError, PasswordMinLengthError
from datetime import datetime as dt
from app.exc.excessoes import DateAlreadyInUseError



def verify_keys(kwargs, option, method="post"):

    options = {
        "location": {'dt_start', 'dt_end', 'id_room', 'id_clinic', 'id_therapist'},
        "room": {'nm_room', 'id_specialty', 'ds_status'},
        "attendant": {'nm_attendant', 'nr_cpf', 'nr_telephone', 'nr_cellphone', 'ds_password', 'id_clinic', 'ds_email'},
        "customer": {'nm_customer', 'nr_cpf', 'nr_rg', 'nm_mother', 'nm_father', 'nr_healthcare', 'ds_address', 'nr_telephone', "nr_cellphone", 'ds_email', 'dt_birthdate'},
        "therapist": {'nm_therapist', 'nr_cpf', 'nr_crm', 'nm_user', 'ds_password', 'ds_specialties', 'nr_cellphone', 'ds_email','ds_status'},
        "clinic": {'nm_clinic', 'nr_cnpj', 'ds_address', 'nr_address', 'ds_complement', 'ds_district', 'nr_zipcode', 'ds_city', 'ds_uf', 'ds_email', 'nr_telephone', 'nr_cellphone'},
        "specialty":{'nm_specialty'},
        "session":{'id_customer', 'id_therapist', 'dt_start', 'dt_end', 'ds_status' },
        "technique":{'nm_technique','dt_start', 'dt_end', 'ds_comment', 'id_therapist', 'nm_customer' },
        "login":{'nr_cpf','ds_password' },
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


def verify_possiblle_dates(query, data):
    if not query:
        return True
    for item in query:
        location_dict = dict(item)
        dt_start_location = location_dict.get('dt_start')
        dt_end_location = location_dict.get('dt_end')        
        dt_start_user = dt.strptime(data.get('dt_start'), "%d/%m/%Y %H:%M:%S")
        dt_end_user = data.get('dt_end')

        
        if not dt_start_user < dt_start_location and not dt_end_user < dt_start_location:            
            raise DateAlreadyInUseError("data já está sendo usada")
        elif not dt_start_user > dt_start_location and not dt_start_user > dt_end_location:
            raise DateAlreadyInUseError("data já está sendo usada")
            
              
            
    
    
