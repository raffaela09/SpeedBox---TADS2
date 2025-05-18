import getpass
import bcrypt
from speedBox_izab3lla import User
from Validations import validate_cpf, validate_email, validate_pwd, validate_user_type
from user_service import User_service

def register_user():
    print("\n------- User Registration --------")
    name = input("Name: ")
    cpf = input("CPF:")
    validate_cpf(cpf)

    email = input("Email: ")
    validate_email(email)

    pwd = getpass.getpass("Password: ") #Masks the password in the prompt
    validate_pwd(pwd)
    encry_pwd = pwd.encode('utf-8') 
    pwd_hash = bcrypt.hashpw(encry_pwd, bcrypt.gensalt())
    pwd_hash_str = pwd_hash.decode('utf-8') #Converts from bytes to string so JSON can accept it
    user_type = input("Type of user (client, deliveryman or manager): ").lower()
    validate_user_type(user_type)

    user_register = User(name, cpf, email, pwd_hash_str, user_type)
    #Here I call the user dict to return it as a dictionary and save everything to the JSON using create_account
    user_to_dict = user_register.user_dic(name, cpf, email, pwd_hash_str, user_type)
    #And here I called the create_account method so it can receive the data as a dictionary and save it into the JSON.
    User_service.create_account(user_to_dict)

def login_user():
    print("\n------- User Login --------")
    email = input("Email: ")
    pwd = getpass.getpass("Password: ")
    
    #Calls the user login function, which will verify
    User_service.login(email,pwd)
    

def cancel_inputs():
    print("\n------- Cancel order --------")
    confirm = input("Deseja concelar o pedido? (yes/no):").lower()
    return confirm == "yes"

def place_order():
    print("\n------- Place Order --------")
    response = input("Do you want to confirm the order? (yes/no): ").lower()
    return response == "yes"

def received():
    print("\n------- Confirm Order Receipt --------")
    received_confirmation = input("Do you want to confirm the delivery? (yes/no): ").lower()
    return received_confirmation == "yes"

    

