from services.OrderService import OrderService
from models.Exceptions import ProductNotFoundError, NoOrdersError
from models.Delivery import Delivery

def accept_order_manager_menu(manager):
    order_service = OrderService('orders.json')
    try:
        order_service.show_informations("on hold")
        code_manager = int(input("Type code of order: "))
        address_manager = input("Enter your address: ")
        delivery_teste = Delivery(address_manager)
        address_manager_coord = delivery_teste.geocode(address_manager)
        manager.schedule_delivery(
            num_order = code_manager, 
            email = manager.email, 
            user_type = manager.user_type, address_manager = address_manager_coord),
        print('Order accepted!')
    except (NoOrdersError, ProductNotFoundError ) as error:
        print(error)
#-----------------------------------------------------------------------------------
            
def cancel_order_manager_menu(manager):
    order_service = OrderService('orders.json')
    try:
        order_service.show_informations("on hold")
        code_manager = input("Enter code of order: ")
        manager.refuse_delivery(
            num_order = code_manager,
            email = manager.email,
            user_type = manager.user_type
            )
        print('Order canceled!')
    except (NoOrdersError, ProductNotFoundError) as error:
            print(error)
#-----------------------------------------------------------------------------------
        
def options_manager(manager):
    order_service = OrderService('orders.json')
    while True:
        print("\n--------Manager---------\n")
        print("\n1 - Accept order.\n2 - Refuse order.\n3 - Show history\n4 - Logout\n")
        answer_manager = input("Type your option: ")
        #caso a opcao seja para aceitar, ele mostra os pedidos com esse codigo
        if answer_manager == "1":
            accept_order_manager_menu(manager)             	
        elif answer_manager == "2":
            cancel_order_manager_menu(manager)
        elif answer_manager == "3":
            order_service.show_history(manager.user_type, manager.email)
        elif answer_manager == "4":
            break
#-----------------------------------------------------------------------------------