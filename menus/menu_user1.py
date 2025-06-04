import getpass
import bcrypt  
from services.UserService import UserService
from models.User import User
from validations.validations import validate_cpf, validate_email, validate_pwd
from models.Exceptions import PasswordOrEmailInvalidError, EmailAlreadyRegisteredError, CpfAlreadyRegisteredError, InvalidEmailError, PasswordInvalidError, CpfInvalidError
from validations.user_validate import validate_email_existing, validate_cpf_existing

#menu_usuari   (fazer login e criar conta)
def register_user():
    try:
        user_service = UserService('users.json')
        print("\n------- User Registration --------")
        name = input("Name: ")
        cpf = input("CPF:")
        validate_cpf(cpf)
        validate_cpf_existing(cpf)

        email = input("Email: ")
        validate_email(email)
        validate_email_existing(email)
        
        pwd = getpass.getpass("Password: ") #Mascara a senha no prompt
        validate_pwd(pwd)
        encry_pwd = pwd.encode('utf-8') 
        pwd_hash = bcrypt.hashpw(encry_pwd, bcrypt.gensalt())#
        pwd_hash_str = pwd_hash.decode('utf-8') #converte de bytes para str para o json poder aceitar

        user_type = input("Type of user (client, deliveryman or manager): ").lower()
        # validate_user_type(user_type)

        user_register = User(name, cpf, email, pwd_hash_str, user_type)
        #aqui eu chamo o user dict pra poder devolver como dicionario e salvar tudo no json com o create_account
        user_to_dict = user_register.user_dic()
        #e aqui chamei o metodo de criar a conta, pra que o metodo possa receber esses dados que estao como dicionario e salva dentro do json.
        user_service.create_account(user_to_dict)
    except (EmailAlreadyRegisteredError, CpfAlreadyRegisteredError, InvalidEmailError, PasswordInvalidError, CpfInvalidError) as error:
        print(error)
        
def login_user():
    user_service = UserService('users.json')
    try:
        print("\n------- User Login --------")
        email = input("Email: ").strip().lower()
        pwd = getpass.getpass("Password: ")
        
        print(f"\nEmail confirmed! Welcome!\n")
        
        #chama a funcao de login do usuario, que vai verificar
        return user_service.login(email,pwd)
    except PasswordOrEmailInvalidError as error:
        print(error)