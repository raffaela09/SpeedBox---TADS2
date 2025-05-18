from speedBox_izab3lla import User
from Exceptions import ProductNotFoundError
from save_json import load_orders, update_json
class DeliveryMan(User):
    def __init__(self, name, cpf, email, pwd, user_type):
        super().__init__(name, cpf, email, pwd, user_type)
    #-----------------------------------------------------------------------------------
      
    def make_delivery(self, num_order):
        orders = load_orders()
        for order in orders:
            if num_order == order["num_order"] and order["status"] == "out for delivery":
                update_json(
                    update_orders={
                        "num_order": num_order, 
                        "status": "order delivered"
                    },
                    keys=["num_order"]
                )
            else:
                pass
    #-----------------------------------------------------------------------------------
    
    def collect_delivery(self, num_order):
        orders = load_orders()
        for order in orders:
            if num_order == order["num_order"] and order["status"] == "awaiting pickup":
                update_json(
                    update_orders={
                        "num_order": num_order, 
                        "status": "out for delivery"
                    },
                    keys=["num_order"]
                )
            else:
                pass
    #-----------------------------------------------------------------------------------

  