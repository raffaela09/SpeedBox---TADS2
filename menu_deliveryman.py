from Exceptions import ProductNotFoundError, NoProductsToDisplayError, TransportInvalidError,NoOrdersError
from service import read, show_history
from speedBox_Julia import Bicycle, Car, Motorcycle

def chose_transport():
    transport = input('Enter the type of transportation you want to use (car, motorcycle, or bicycle): ')
    if transport == 'car':
        return Car
    
    elif transport == 'motorcycle':
        return Motorcycle
    
    elif transport == 'bicycle':
        return Bicycle
    else:
        raise TransportInvalidError('Invalid transport option.')

def make_delivery_menu(deliveryman):
    try:
        read("out for delivery")
        code_deliveryman = input("Type code of order: ")
        deliveryman.make_delivery(
            num_order = code_deliveryman, 
            email = deliveryman.email, 
            user_type = deliveryman.user_type)
    except (ProductNotFoundError, NoOrdersError) as error:
            print(error)
            
def collect_delivery_menu(deliveryman):
    try:
        read("awaiting pickup")
        transport = chose_transport()
        code_deliveryman = input("Type code of order: ")
        deliveryman.collect_delivery(
                num_order = code_deliveryman,
                email = deliveryman.email,
                user_type = deliveryman.user_type,
                transport = transport
            )
        transport_instance = transport()
        deliveryman.transport = transport_instance
    except (NoOrdersError, ProductNotFoundError, TransportInvalidError) as error:
            print(error)
            
def options_deliveryman(delivery_man):
    print("\n--------DeliveryMan---------\n")
    print("\n1 - Pick up order.\n2 - Make a delivery.\n3 - Show history.\n4 - Logout\n")
    answer_delivery_man = input("Type your option: ")
    if answer_delivery_man == "1":
        collect_delivery_menu(delivery_man)
    elif answer_delivery_man == "2":
        make_delivery_menu(delivery_man)
    elif answer_delivery_man == "3":
        try:
            show_history(delivery_man.user_type, delivery_man.email)
        except NoProductsToDisplayError as error:
            print(error)