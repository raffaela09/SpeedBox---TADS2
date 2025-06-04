import re 
from models.Exceptions import InvalidEmailError, PasswordInvalidError, CpfInvalidError

def validate_pwd(pwd):
    if len(pwd) < 6:
        raise PasswordInvalidError("The password must be at least 6 characters long.")
    
def validate_cpf(cpf):
    if len(cpf) != 11 or len(set(cpf)) == 1:# Checks if it has a number different from 11 digits
# or if all the digits are the same
        raise CpfInvalidError("Invalid CPF!") #lancei o raise pra caso estiver errado ele nao permitir a continuacao do cadastro

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        raise InvalidEmailError("Invalid email format.")
