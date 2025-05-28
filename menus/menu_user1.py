import getpass
import bcrypt
from speedBox_izab3lla import User
from validations import validate_cpf, validate_email, validate_pwd
from models.Exceptions import CodeAlreadyExisitError, NoProductsToDisplayError
from speedBox_Julia import Order
from services.service import show_history

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
    

def place_order_2(client):
    try:
        print("\n------- Place Order --------")
        num_order = input("Code of order: ")
        product = input("Product: ")
        distance = int(input("Enter distance: "))
        order = Order(num_order, client)
        date_dic_order = order.dic_order(client.email, num_order, product, distance)
        client.request_delivery(date_dic_order)
    except CodeAlreadyExisitError as error:
        print(error)
def options_user(client):
    while True:
        print("1 - Place Order\n2 - Show history.\n3 - Logout.")
        answer_client = input("Enter your option: ")
        if answer_client == "1":
            try:
                place_order_2(client)
            except NoProductsToDisplayError as error:
                print(error)
        elif answer_client == "2":
            show_history(client.user_type, client.email)
        elif answer_client == "3":
            break
def received():
    print("\n------- Confirm Order Receipt --------")
    received_confirmation = input("Do you want to confirm the delivery? (yes/no): ").lower()
    return received_confirmation == "yes"