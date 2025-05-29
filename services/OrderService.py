from services.Service import Service
from models.Exceptions import NoOrdersError, ProductNotFoundError, NoProductsToDisplayError
class OrderService(Service):
    def __init__(self, name_file):
        super().__init__(name_file)
    #daqui pra baixo service do pedido
    
    def show_informations(self, mensage):
        orders = self.load_data()
        found = False
        for order in orders:
            if order["status"] == mensage:
                print(f"ORDERS {mensage.upper()}:\nClient: {order["cliente"]}\nCode: {order["num_order"]}\nProduct: {order["name_product"]}\nDistance: {order["distance"]}")
                found = True
                break
        if not found:
            raise NoOrdersError(f"No orders in {mensage}.")

    def change_status(self, number_order, email_user, mensage_status_search, mensage_status_update, type_user_key):
        orders = self.load_data()
        found = False
        for order in orders:
            if number_order == order["code"] and order["status"] == mensage_status_search:
                self.update_json(
                    update_orders = {
                    "num_order": number_order,
                    "status": mensage_status_update,
                    type_user_key: email_user
                    },
                keys = ["num_order"]
                )
                
                found = True
                break
        
        if not found:
            raise ProductNotFoundError("Order not found or status did not match.")
                
    def show_history(self, type_user, email_user):
        orders = self.load_data()

        found = False
        for order in orders:
            if type_user in order and order[type_user] == email_user:
                print(f"\nCode order: {order['code']}\nProduct: {order['product']}\nDistance: {order['address_client']}\nStatus: {order['status']}\n")
                found = True
                break
        if not found:
            raise NoProductsToDisplayError("There are no orders to display.")
    
