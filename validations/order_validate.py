from services.OrderService import OrderService
from models.Exceptions import CodeAlreadyExisitError
ORDER_SERVICE = OrderService('orders.json')

def validate_code(code):
    orders = ORDER_SERVICE.load_data()
    
    for order in orders:
        if order['code'] == code:
            raise CodeAlreadyExisitError
    return True