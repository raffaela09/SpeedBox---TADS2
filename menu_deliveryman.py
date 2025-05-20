from Exceptions import ProductNotFoundError
from save_json import read


def make_delivery_menu(deliveryman):
    read("out for delivery")
    code_deliveryman = input("Type code of order: ")
    if code_deliveryman:
        try:
            deliveryman.make_delivery(
            num_order = code_deliveryman, 
            email = deliveryman.email, 
            user_type = deliveryman.user_type)
        except ProductNotFoundError as error:
            print(error)
            
def collect_delivery_menu(deliveryman):
    read("awaiting pickup")
    code_deliveryman = input("Type code of order: ")
    if code_deliveryman:
        try:
            deliveryman.collect_delivery(
                num_order = code_deliveryman,
                email = deliveryman.email,
                user_type = deliveryman.user_type
            )
        except ProductNotFoundError as error:
            print(error)