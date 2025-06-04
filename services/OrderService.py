from services.Service import Service
from models.Exceptions import NoOrdersError, ProductNotFoundError, NoProductsToDisplayError
class OrderService(Service):
    def __init__(self, name_file):
        super().__init__(name_file)
        
    def show_informations(self, mensage: str):
        orders = self.load_data()
        found = False
        informations = []
        for order in orders:
            if order["status"] == mensage:
                #prints dentro do service nao sao ideais, mas facilita os testes, entao vou deixar assim
                found = True
                informations.append(order)
        if not found:
            raise NoOrdersError(f"No orders in {mensage}.")
        return informations

    def change_status(self, number_order: int, email_user: str, mensage_status_search: str, mensage_status_update: str, type_user_key: str):
        orders = self.load_data()
        found = False
        for order in orders:
            if int(number_order) == order["code"] and order["status"] == mensage_status_search:
                self.update_json(
                    update_data = {
                    "code": order["code"],
                    "status": mensage_status_update,
                    type_user_key: email_user
                    },
                keys = ["code"]
                )
                
                found = True
                break
        
        if not found:
            raise ProductNotFoundError("Order not found or status did not match.")
     
#                print(f"\nCode order: {order['code']}\nProduct: {order['product']}\nDistance: {order['address_client']}\nStatus: {order['status']}\nPayment method: {order['payment']['method']}\nPayment status: {order['payment']['status']}\n")# tirar print do service - passa pro menu                
    def show_history(self, type_user: str, email_user: str):
        orders = self.load_data()
        history = []
        found = False
        for order in orders:
            if type_user in order and order[type_user] == email_user:
                found = True
                history.append(order)

        if not found:
            raise NoProductsToDisplayError("There are no orders to display.")
        return history
