from speedBox_izab3lla import User
from services.OrderService import OrderService
from speedBox_Julia import Transport
from services.DeliveryService import DeliveryService
class DeliveryMan(User):
    def __init__(self, name, cpf, email, pwd, user_type):
        super().__init__(name, cpf, email, pwd, user_type)
    #-----------------------------------------------------------------------------------
    #passar para o service do delivery, criar a classe do delivery, onde consome a api
    def make_delivery(self, num_order, email, user_type):
        DeliveryService.make_delivery(num_order, email, user_type)
        
    #-----------------------------------------------------------------------------------

    def collect_delivery(self, num_order, email, user_type, transport):
       DeliveryService.collect_delivery(num_order, email, user_type, transport)
    #-----------------------------------------------------------------------------------
