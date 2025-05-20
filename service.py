#aqui deveria ser uma classe de service, mas eu teria que mudar todo o resto, e nao temos mais tempo
from Exceptions import ProductNotFoundError, NoProductsToDisplayError, NoOrdersError
import json
    
# Implementing JSON to save the user
def load_users():#loads the existing users
    try:
        with open("users.json", "r") as file:
            return json.load(file) 
    except FileNotFoundError:
        return [] 


def save_users(users): #saves in a list
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

def load_orders():
    try:
        with open("orders.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_orders(orders):
    with open("orders.json", "w") as file:
        json.dump(orders, file, indent=4)
        
def update_json(update_orders, keys):
    data = load_orders()
    
    found = False 
    
    for item in data:
        match = True
        
        for key in keys:
            if item.get(key) != update_orders.get(key):
                match = False
                break
            if match:
                item.update(update_orders)
                found = True
                break
    if not found:
        pass
        #lancar raise aqui
    with open("orders.json", "w") as file:
        json.dump(data, file, indent=4)
        
def read(msg):
        orders = load_orders()
        found = False
        for order in orders:
            if order["status"] == msg:
                print(f"ORDERS {msg.upper()}:\nClient: {order["cliente"]}\nCode: {order["num_order"]}\nProduct: {order["name_product"]}\nDistance: {order["distance"]}")
                found = True
                break
        if not found:
            raise NoOrdersError(f"No orders in {msg}.")

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
    found = False
    for order in orders:
        if type_user in order and order[type_user] == email_user:
            print(f"\nCode order: {order['num_order']}\nProduct: {order['name_product']}\nDistance: {order['distance']}\nStatus: {order['status']}\n")
            found = True
            break
    if not found:
        raise NoProductsToDisplayError("There are no orders to display.")