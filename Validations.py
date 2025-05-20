import re
from Exceptions import InvalidateEmailError
def validate_pwd(pwd):
    if len(pwd) < 6:
        print("The password must be at least 6 characters long.")
        return False
    
def validate_cpf(cpf):
    if len(cpf) != 11 or len(set(cpf)) == 1:# Checks if it has a number different from 11 digits
# or if all the digits are the same
        print("Invalid CPF!")
        return False

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        raise InvalidateEmailError("Invalid email format.")