<<<<<<< HEAD
import re
from models.Exceptions import InvalidateEmailError
=======
from save_json import load_users

>>>>>>> origin/izab3lla-branch
def validate_pwd(pwd):
    if len(pwd) < 6:
        raise ValueError("The password must be at least 6 characters long.")
    
def validate_cpf(cpf):
    if len(cpf) != 11 or len(set(cpf)) == 1:# Checks if it has a number different from 11 digits
# or if all the digits are the same
<<<<<<< HEAD
        print("Invalid CPF!")
        return False

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        raise InvalidateEmailError("Invalid email format.")
=======
        raise ValueError("Invalid CPF!")
        
def validate_email(email):
    users = load_users()
    for user in users:
        if email == user["email"]:
            raise ValueError("Email already registered")
        
def validate_user_type(user_type):
    valid_types = ["client", "deliveryman", "manager"]
    if user_type.lower() not in valid_types:
        raise ValueError("Invalid user type. Please choose from: client, deliveryman or manager.")
        
>>>>>>> origin/izab3lla-branch
