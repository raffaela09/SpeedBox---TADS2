from services.Service import Service
from services.OrderService import OrderService
from models.Exceptions import ItemNotFoundError

class DeliveryService(Service):
    def __init__(self, name_file):
        super().__init__(name_file)
        
    def make_delivery(self, num_order, email, user_type): 
        order_service = OrderService("orders.json")
        order_service.change_status(
            number_order = num_order, 
            email_user = email,
            mensage_status_search = "out for delivery",
            mensage_status_update = "order deliveried",
            type_user_key = user_type
        )
        
        orders = self.load_data()
        
        for order in orders:
            if int(order['code'] == int(num_order)):
                payment = order['payment']
                if payment['status'] == 'awaiting':
                    order['payment']['status'] = 'paid'
                    order_service.update_json(order, ['code'])
    #-----------------------------------------------------------------------------------
    
    def collect_delivery(self, num_order, email, user_type, transport, address_delivery_man, estimated_time, km):
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
                order['estimated_time'] = estimated_time
                order['km'] = km
                order["code"] = int(order["code"])
                order_service.update_json(order, ['code'])
                break
       else:
                raise ItemNotFoundError(f"Order with code {num_order} not found.")