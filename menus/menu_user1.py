import getpass
import bcrypt
from speedBox_izab3lla import User
from validations import validate_cpf, validate_email, validate_pwd

#menu_usuario (fazer login e criar conta)
def register_user():
    print("\n------- User Registration --------")
    name = input("Name: ")
    cpf = input("CPF:")
    validate_cpf(cpf)

    email = input("Email: ")
    validate_email(email)

    pwd = getpass.getpass("Password: ") #Mascara a senha no prompt
    validate_pwd(pwd)
    encry_pwd = pwd.encode('utf-8') 
    pwd_hash = bcrypt.hashpw(encry_pwd, bcrypt.gensalt())#
    pwd_hash_str = pwd_hash.decode('utf-8') #converte de bytes para str para o json poder aceitar

    user_type = input("Type of user (client, deliveryman or manager): ").lower()
    # validate_user_type(user_type)

    user_register = User(name, cpf, email, pwd_hash_str, user_type)
    #aqui eu chamo o user dict pra poder devolver como dicionario e salvar tudo no json com o create_account
    user_to_dict = user_register.user_dic(name, cpf, email, pwd_hash_str, user_type)
    #e aqui chamei o metodo de criar a conta, pra que o metodo possa receber esses dados que estao como dicionario e salva dentro do json.
    User.create_account(user_to_dict)

def login_user():
    print("\n------- User Login --------")
    email = input("Email: ")
    pwd = getpass.getpass("Password: ")
    
    #chama a funcao de login do usuario, que vai verificar
    return User.login(email,pwd)