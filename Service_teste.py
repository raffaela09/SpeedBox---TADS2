#aqui deveria ser uma classe de service, mas eu teria que mudar todo o resto, e nao temos mais tempo
from Exceptions import ProductNotFoundError

def change_status(number_order, email_user, mensage_status_search, mensage_status_update, type_user_key):
    orders = load_orders()
    found = False
    for order in orders:
        if number_order == order["num_order"] and order["status"] == mensage_status_search:
            update_json(
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
            
def show_history(type_user, email_user):
    orders = load_orders()
    if orders:
        for order in orders:
            if type_user in order and order[type_user] == email_user:
                print(f"\nCode order: {order["num_order"]}\nProduct:  {order["name_product"]}\nDistance: {order["distance"]}\nStatus: {order["status"]}\n")
    else:
        raise NoProductsToDisplayError("There are no orders to display.")