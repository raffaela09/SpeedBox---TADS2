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
    confirm = input("Deseja concelar o pedido? (yes/no):").lower()
    return confirm == "yes"

def place_order():
    print("------- Place Order --------")
    response = input("Do you want to confirm the order? (yes/no): ").lower()
    return response == "yes"

def received():
    print("------- Confirm Order Receipt --------")
    received_confirmation = input("Do you want to confirm the delivery? (yes/no): ").lower()
    return received_confirmation == "yes"

    

