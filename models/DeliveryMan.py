from speedBox_izab3lla import User
from services.service import change_status, load_orders, update_json
from speedBox_Julia import Transport
class DeliveryMan(User):
    def __init__(self, name, cpf, email, pwd, user_type):
        super().__init__(name, cpf, email, pwd, user_type)
    #-----------------------------------------------------------------------------------
      
    def make_delivery(self, num_order, email, user_type):
        change_status(
            number_order = num_order, 
            email_user = email,
            mensage_status_search = "out for delivery",
            mensage_status_update = "order deliveried",
            type_user_key = user_type
        )
            #(self, number_order, mensage_status, keys, talvez exception )
    #-----------------------------------------------------------------------------------
    
    def collect_delivery(self, num_order, email, user_type, transport):
       change_status(
           number_order= num_order,
           email_user = email,
           mensage_status_search = "awaiting pickup",
           mensage_status_update = "out for delivery",
           type_user_key = user_type
       )
       orders = load_orders()
       for order in orders:
          if order['num_order'] == num_order:
            order['transport'] = transport.__name__
            order['estimated_time'] = transport.estimated_time(distance = order['distance'])
            update_json(order, ['code'])
            print(f'Time estimated: {order['estimated_time']}')
    #-----------------------------------------------------------------------------------
