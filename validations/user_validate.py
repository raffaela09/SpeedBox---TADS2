from services.UserService import UserService
from models.Exceptions import EmailAlreadyRegisteredError, CpfAlreadyRegisteredError
USER_SERVICE = UserService('users.json')

def validate_email_existing(email):
    users = USER_SERVICE.load_data()
    
    for user in users:
        if user['email'] == email:
            raise EmailAlreadyRegisteredError(f'E-mail: {email} already registered.')
    return True

def validate_cpf_existing(cpf):
    users = USER_SERVICE.load_data()
    
    for user in users:
        if user['cpf'] == cpf:
            raise CpfAlreadyRegisteredError(f'CPF already registered.')
    return True