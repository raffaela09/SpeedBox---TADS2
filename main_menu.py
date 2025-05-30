from menus.menu_user1 import register_user, login_user
from speedBox_izab3lla import Client
from models.ManagerBusiness import ManagerBusiness
from models.DeliveryMan import DeliveryMan
from menus.menu_manager import options_manager
from menus.menu_deliveryman import options_deliveryman
from menus.menu_client import options_user
from services.Service import Service

while True:
    print("\n--------Welcome!!---------\n")
    print("1 - Create account.\n2 - Login.\n3 - Logout.\n") #trocar a ser
    option = input("Enter your option: ")
    if option == "1":
        register_user()
        
    #opcao de fazer login
    elif option =="2":
        FILE_USER = Service("users.json")
        users = FILE_USER.load_data()
        user_data = login_user()

        if user_data and user_data["type_user"] == "cliente":
                client = Client(
                    name = user_data["name"],
                    cpf= user_data["cpf"],
                    email= user_data["email"],
                    pwd = user_data["pwd"],
                    user_type= user_data["type_user"],
                    orders= []
                )
                options_user(client)
        elif user_data and user_data["type_user"] == "gerente":
            manager = ManagerBusiness(
                name = user_data["name"],
                cpf= user_data["cpf"],
                email= user_data["email"],
                pwd = user_data["pwd"],
                user_type= user_data["type_user"],
                )
            
            options_manager(manager)
        elif user_data and user_data["type_user"] == "entregador":
            delivery_man = DeliveryMan(
                    name = user_data["name"],
                    cpf= user_data["cpf"],
                    email= user_data["email"],
                    pwd = user_data["pwd"],
                    user_type= user_data["type_user"],
                )
            
            options_deliveryman(delivery_man)
                    
    elif option == '3':
        print("Until next time.")
        break
    else:
        print("Invalid option, please try again.")