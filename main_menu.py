from menus.menu_user1 import register_user, login_user, options_user
from speedBox_izab3lla import Client
from models.ManagerBusiness import ManagerBusiness
from models.DeliveryMan import DeliveryMan
from menus.menu_manager import options_manager
from menus.menu_deliveryman import options_deliveryman
from services.service import load_users

while True:
    print("\n--------Welcome!!---------\n")
    print("1 - Create account.\n2 - Login.\n3 - Logout.\n")
    option = input("Enter your option: ")
    if option == "1":
        register_user()
        
    #opcao de fazer login
    elif option =="2":
        users = load_users()
        user_data = login_user()
        #separei aqui pra ja chamar os menus de acordo com os clientes (tipo de cliente que ele digita no cadastro)
        #verifica se os dados estao sendo retornados e o tipo do usuario pra passar o menu de cada usuario
        #
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
                #termina de implementar o restante aqui
                
        #num_order, email, user_type        
        #minha parte         
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