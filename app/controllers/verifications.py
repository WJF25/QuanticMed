from app.exc.excessoes import WrongKeyError
from app.exc.excessoes import NoExistingValueError

def verify_keys(kwargs, option, method="post"):
    
    options = {
        "location":{'dt_start','dt_end', 'id_room', 'id_clinic', 'id_therapist'},
        "room":{'nm_room', 'id_specialty'},
        "attendant":{'nm_attendant', 'nr_cpf', 'nr_telephone', 'nr_cellphone', 'ds_password', 'dt_creation_time', 'id_clinic'},
        "customer":{'nm_customer','nr_cpf', 'nr_rg','nm_mother', 'nm_father', 'nr_healthcare', 'ds_address', 'nr_telephone', "nr_cellphone", 'ds_email', 'dt_birthdate'}
    }

    keys = set(kwargs.keys())

    if method == "post":
        if len(keys) == 0:
            raise WrongKeyError({"Chaves Disponíveis":list(options[option])})
        elif not options[option].issubset(keys):
            error = list(keys - options[option] )
            
            raise WrongKeyError({"Chaves_erradas":error, "Chaves Disponíveis":list(options[option])})
        else:
            error = list(keys - options[option] )
            raise WrongKeyError({"Chaves_erradas":error, "Chaves Disponíveis":list(options[option])})
        
                    
    else:
        
        if not keys.issubset(options[option]):
            error = list(keys - options[option])
            raise WrongKeyError({"Chaves_erradas":error, "Chaves Disponíveis":list(options[option])})
        elif options[option].issubset(keys):
            error = list(keys - options[option] )
            raise WrongKeyError({"Chaves_erradas":error, "Chaves Disponíveis":list(options[option])})            

        else:
            return True


def verify_none_values(value):
    if value == None:
        raise NoExistingValueError({"Erro": "Informação não existe no banco de dados"})


