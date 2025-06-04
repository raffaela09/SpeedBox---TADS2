from services.OrderService import OrderService
from models.Exceptions import ProductNotFoundError, NoOrdersError, NoProductsToDisplayError
from models.Delivery import Delivery

def accept_order_manager_menu(manager):
    order_service = OrderService('orders.json')
    try:
        orders = order_service.show_informations("on hold")
        for order in orders:
            print(f"ORDERS ON HOLD:\nClient: {order['client']}\nCode: {order['code']}\nProduct: {order['product']}\n")
        code_manager = int(input("Type code of order: "))
        address_manager = input("Enter your address: ")
        delivery_teste = Delivery(address_manager)
        address_manager_coord = delivery_teste.geocode(address_manager)
        manager.schedule_delivery(
            num_order = code_manager, 
            email = manager.email, 
            user_type = manager.user_type, address_manager = address_manager_coord)
        print('Order accepted!')
    except (NoOrdersError, ProductNotFoundError ) as error:
        print(error)
#-----------------------------------------------------------------------------------
            
def cancel_order_manager_menu(manager):
    order_service = OrderService('orders.json')
    try:
        orders = order_service.show_informations("on hold")
        for order in orders:
            print(f"ORDERS ON HOLD:\nClient: {order['client']}\nCode: {order['code']}\nProduct: {order['product']}\n")
        code_manager = input("Enter code of order: ")
        manager.refuse_delivery(
            num_order = code_manager,
            email = manager.email,
            user_type = manager.user_type)
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
            try:
                orders= order_service.show_history(manager.user_type, manager.email)
                for order in orders: 
                     print(f"\nCode order: {order['code']}\nProduct: {order['product']}\nDistance: {order['address_client']}\nStatus: {order['status']}\nPayment method: {order['payment']['method']}\nPayment status: {order['payment']['status']}\n")
            except NoProductsToDisplayError as error:
                print(error)
        elif answer_manager == "4":
            break
#-----------------------------------------------------------------------------------