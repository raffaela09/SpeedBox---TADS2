from services.OrderService import OrderService
from models.Exceptions import ProductNotFoundError, NoOrdersError


def accept_order_manager_menu(manager):
    try:
        OrderService.show_informations("on hold", "orders.json")
        code_manager = input("Type code of order: ")
        manager.schedule_delivery(
            num_order = code_manager, 
            email = manager.email, 
            user_type = manager.user_type)
    except (NoOrdersError, ProductNotFoundError ) as error:
        print(error)

            
def cancel_order_manager_menu(manager):
    try:
        OrderService.show_informations("on hold", "orders.json")
        code_manager = input("Type code of order: ")
        manager.refuse_delivery(
            num_order = code_manager,
            email = manager.email,
            user_type = manager.user_type
            )
    except (NoOrdersError, ProductNotFoundError) as error:
            print(error)
        
def options_manager(manager):
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
            OrderService.show_history(manager.user_type, manager.email)
        elif answer_manager == "4":
            break