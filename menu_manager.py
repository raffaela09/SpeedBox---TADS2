from Exceptions import ProductNotFoundError
from save_json import read

def accept_order_manager_menu(manager):
    read("on hold")
    code_manager = input("Type code of order: ")
    if code_manager:
        try:
            manager.schedule_delivery(
            num_order = code_manager, 
            email = manager.email, 
            user_type = manager.user_type)
        except ProductNotFoundError as error:
            print(error)
            
def cancel_order_manager_menu(manager):
    read("on hold")
    code_manager = input("Type code of order: ")
    if code_manager:
        try:
            manager.refuse_delivery(
                num_order = code_manager,
                email = manager.email,
                user_type = manager.user_type
            )
        except ProductNotFoundError as error:
            print(error)