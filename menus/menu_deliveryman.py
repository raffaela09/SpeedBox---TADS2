from models.Exceptions import ProductNotFoundError, NoProductsToDisplayError, TransportInvalidError,NoOrdersError
from services.OrderService import OrderService
from speedBox_Julia import Bicycle, Car, Motorcycle
from models.Delivery import Delivery

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
    order_service = OrderService("orders.json")
    try:
        order_service.show_informations("out for delivery")
        code_deliveryman = input("Type code of order: ")
        deliveryman.make_delivery(
            num_order = code_deliveryman, 
            email = deliveryman.email, 
            user_type = deliveryman.user_type)
    except (ProductNotFoundError, NoOrdersError) as error:
            print(error)
            
def collect_delivery_menu(deliveryman):
    order_service = OrderService("orders.json")
    json_load = order_service.load_data()
    try:
        order_service.show_informations("awaiting pickup")
        transport = chose_transport()
        code_deliveryman = int(input("Enter code of order: "))
        address_delivery_man = input("Enter your address: ")
        delivery_teste = Delivery(address_delivery_man)
        addres_delivery_man_coords = delivery_teste.geocode(address_delivery_man)
        deliveryman.collect_delivery(
                num_order = code_deliveryman,
                email = deliveryman.email,
                user_type = deliveryman.user_type,
                transport = transport,
                address_delivery_man = addres_delivery_man_coords,
            )
        for item in json_load:
            if item['code'] == code_deliveryman:
    
                print(item['address_client'])
                distance_manager_client, time_manager_client = delivery_teste.distance_time(item['address_client'], item['address_manager'])
                print(distance_manager_client, time_manager_client)
        transport_instance = transport()
        deliveryman.transport = transport_instance
    except (NoOrdersError, ProductNotFoundError, TransportInvalidError) as error:
            print(error)
            
def options_deliveryman(delivery_man):
    order_service = OrderService("orders.json")
    print("\n--------DeliveryMan---------\n")
    print("\n1 - Pick up order.\n2 - Make a delivery.\n3 - Show history.\n4 - Logout\n")
    answer_delivery_man = input("Type your option: ")
    if answer_delivery_man == "1":
        collect_delivery_menu(delivery_man)
    elif answer_delivery_man == "2":
        make_delivery_menu(delivery_man)
    elif answer_delivery_man == "3":
        try:
            order_service.show_history(delivery_man.user_type, delivery_man.email)
        except NoProductsToDisplayError as error:
            print(error)