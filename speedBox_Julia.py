from abc import ABC, abstractmethod
from service import load_orders
#
class Delivery:
    def __init__(self, status: str, client, rider, pickup: str, destination: str, distance: int):
        self._status = status 
        self._client = client
        self._rider = rider
        self._pickup = pickup
        self._destination = destination
        self._distance = distance
        
    def calculate_estimated_time(self):
        pass

#passar na criacao do entregador, 
class Transport(ABC):
    @abstractmethod
    def estimated_time(distance):
        pass
    
class Car(Transport):
    
    def estimated_time(distance):
        return distance / 100
    
    
class Motorcycle(Transport):
    
    def estimated_time(distance):
        return distance / 80
    
    
class Bicycle(Transport):
    
    def estimated_time(distance):
        return distance / 20
        
class Payment(ABC): 
    @abstractmethod
    def confirm_payment(self):
        pass
    def refund_payment(self):
        pass
    def payment_receipt(self):
        pass 
    
class Credit(Payment):
    def confirm_payment(self):
        pass
    def refund_payment(self):
        pass
    def payment_receipt(self):
        pass 
    def pay_in_installments(self):
        pass

class Debit(Payment):
    def confirm_payment(self):
        pass
    def refund_payment(self):
        pass
    def payment_receipt(self):
        pass 

class Pix(Payment):
    def __init__(self, pix_key: str):
        self._pix_key = pix_key
    
    def confirm_payment(self):
        pass
    def refund_payment(self):
        pass
    def payment_receipt(self):
        pass 

class Cash(Payment):
    def confirm_payment(self):
        pass
    def refund_payment(self):
        pass
    def payment_receipt(self):
        pass 
    def calculate_change(self):
        pass
  
 
#fiz a associacao entre cliente e pedido, visto que Cliente pode TER um pedido, entao seria a relacao de associacao.
class Order:
    def __init__(self, order_num: int, client): 
        self._order_num = order_num
        self.client = client
    #retorna os dados do pedido dentro de um dicionario, pra gente poder passar pro json e criar o pedido dentro do json    
    def dic_order(self, email, num_order, name_product, distance):
        return{
            "cliente": email,
            "num_order": num_order,
            "name_product": name_product,
            "distance": distance,
            "status": "on hold" #em espera, ou seja aguardando o gerente aceitar o pedido, para que possa dar procedencia
        }  
    def create(self):
        pass
    #deixei a criacao do pedido dentro de cliente, já que ele é responsavel por criar o pedido, o pedido n é criado sozinho
    #aqui talvez seja a mesma coisa, mas talvez fique realmente aqui pra poder reutilizar
    #ver o historico basicamente.
    
    #verificar esse update, ja que essa funcao vai ser mt importante pras demais coisas, pra atualizar status etc
    def update(self):
        pass
    def delete(self):
        pass