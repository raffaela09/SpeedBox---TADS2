from speedBox_izab3lla import User

def login_user():
    print("------- User Login --------")
    email = input("Email: ")
    pwd = input("Password: ")
    return email, pwd


def register_user():
    print("------- User Registration --------")
    name = input("Name: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    pwd = input("Password: ")
    return name, cpf, email, pwd


def access_type():
    pass

def cancel_input():
    print("------- Cancel order --------")
    confirm = input("Deseja concelar o pedido? (yes/no):").lower
    return confirm == "yes"
    

