from services.Service import Service
from services.OrderService import OrderService
from models.Exceptions import ItemNotFoundError

class DeliveryService(Service):
    def __init__(self, name_file):
        super().__init__(name_file)
        
        #passar para o service do delivery, criar a classe do delivery, onde consome a api
    def make_delivery(self, num_order, email, user_type): 
        order_service = OrderService("orders.json")
        order_service.change_status(
            number_order = num_order, 
            email_user = email,
            mensage_status_search = "out for delivery",
            mensage_status_update = "order deliveried",
            type_user_key = user_type
        )
            #(self, number_order, mensage_status, keys, talvez exception )
    #-----------------------------------------------------------------------------------
    
    def collect_delivery(self, num_order, email, user_type, transport, address_delivery_man):
       order_service = OrderService("orders.json")
       order_service.change_status(
           number_order = num_order,
           email_user = email,
           mensage_status_search = "awaiting pickup",
           mensage_status_update = "out for delivery",
           type_user_key = user_type
       )
       orders = order_service.load_data()
       for order in orders:
            if int(order['code']) == int(num_order):
                # order['estimated_time'] = transport.estimated_time(distance = order['distance'])
                order['address_delivery_man'] = address_delivery_man
                order["code"] = int(order["code"])
                order_service.update_json(order, ['code'])
                break
       else:
                raise ItemNotFoundError(f"Order with code {num_order} not found.")