from services.Service import Service
from services.OrderService import OrderService
from models.Exceptions import ItemNotFoundError

class DeliveryService(Service):
    def __init__(self, name_file):
        super().__init__(name_file)
        
        #passar para o service do delivery, criar a classe do delivery, onde consome a api
    def make_delivery(self, num_order, email, user_type):
        OrderService.change_status(
            number_order = num_order, 
            email_user = email,
            mensage_status_search = "out for delivery",
            mensage_status_update = "order deliveried",
            type_user_key = user_type
        )
            #(self, number_order, mensage_status, keys, talvez exception )
    #-----------------------------------------------------------------------------------
    
    def collect_delivery(self, num_order, email, user_type, transport):
       OrderService.change_status(
           number_order= num_order,
           email_user = email,
           mensage_status_search = "awaiting pickup",
           mensage_status_update = "out for delivery",
           type_user_key = user_type
       )
       orders = self.load_data()
       for order in orders:
          if order['num_order'] == num_order:
            order['transport'] = transport.__name__
            order['estimated_time'] = transport.estimated_time(distance = order['distance'])
            self.update_json(order, ['code'])
            print(f'Time estimated: {order['estimated_time']}')
       else:
            raise ItemNotFoundError(f"Order with code {num_order} not found.")