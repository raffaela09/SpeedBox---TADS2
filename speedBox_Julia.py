from abc import ABC, abstractmethod
from datetime import datetime
from save_json import load_orders, save_orders, update_json
from speedBox_izab3lla import Client
from DeliveryMan import DeliveryMan

class Delivery:
    def __init__(self, status: str, client: Client, deliveryMan: DeliveryMan, pickup: str, destination: str, distance: int):
        self.__status = status 
        self.__client = client
        self.__deliveryMan = deliveryMan
        self.__pickup = pickup
        self.__destination = destination 
        self.__distance = distance
        
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        self.__status = value 
        
    @property
    def client(self):
        return self.__client
    
    @client.setter
    def client(self, value):
        self.__client = value
        
    @property
    def driver(self):
        return self.__driver
    
    @driver.setter
    def driver(self, value):
        self.__driver = value
        
    @property
    def pickup(self):
        return self.__pickup
    
    @pickup.setter
    def pickup(self, value):
        self.__pickup = value
        
    @property
    def destination(self):
        return self.__destination
    
    @destination.setter
    def destination(self, value):
        self.__destination = value  
        
    @property
    def distance(self):
        return self.__distance
    
    @distance.setter
    def distance(self, value):
        self.__distance = value       

class Transport(ABC):
    @abstractmethod
    def estimated_time(self, distance):
        pass  # consumir api google maps 
    
class Motorcyle(Transport):
    def __init__(self, license_plate: str, price_per_km: float, average_speed: float):
        self.__license_plate = license_plate
        self.__price_per_km = price_per_km
        self.average_speed = average_speed
    
    @property
    def license_plate(self):
        return self.__license_plate
    
    @license_plate.setter
    def license_plate(self, value):
        self.__license_plate = value 
        
    @property
    def price_per_km(self):
        return self.__price_per_km
    
    @price_per_km.setter
    def price_per_km(self, value):
        self.__price_per_km = value 
    
    def estimated_time(self, distance):
        return distance / self.average_speed
    
    def total_price(self, distance):
        return distance / self.price_per_km

class Car(Transport):
    def __init__(self, license_plate: str, price_per_km: float, average_speed: float):
        self.__license_plate = license_plate
        self.__price_per_km = price_per_km
        self.average_speed = average_speed
    
    @property
    def license_plate(self):
        return self.__license_plate
    
    @license_plate.setter
    def license_plate(self, value):
        self.__license_plate = value 
        
    @property
    def price_per_km(self):
        return self.__price_per_km
    
    @price_per_km.setter
    def price_per_km(self, value):
        self.__price_per_km = value 
    
    def estimated_time(self, distance):
        return distance / self.average_speed
    
    def total_price(self, distance):
        return distance / self.price_per_km

class Bicycle(Transport):
    def __init__(self, price_per_km: float, average_speed: float):
        self.__price_per_km = price_per_km
        self.average_speed = average_speed
    
    @property
    def price_per_km(self):
        return self.__price_per_km
    
    @price_per_km.setter
    def price_per_km(self, value):
        self.__price_per_km = value 
    
    def estimated_time(self, distance):
        return distance / self.average_speed
    
    def total_price(self, distance):
        return distance / self.price_per_km

# rever a necessidade de mercadoria 
class Merchandise:
    def __init__(self, weight: float, size: float, fragile: bool, package: str, delivery_status: str):
        self.__weight = weight
        self.__size = size 
        self.__fragile = fragile
        self.__package = package
        self.__delivery_status = delivery_status
        
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        self.__weight = value 
        
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        self.__size = value 
        
    @property
    def fragile(self):
        return self.__fragile
    
    @fragile.setter
    def fragile(self, value):
        self.__fragile = value 
        
    @property
    def package(self):
        return self.__package
    
    @package.setter
    def package(self, value):
        self.__package = value 
        
    @property
    def delivery_status(self):
        return self.__delivery_status
    
    @delivery_status.setter
    def delivery_status(self, value):
        self.__delivery_status = value 
        
class Payment(ABC): 
    def __init__(self, value: float):
        self.value = value
        self.confirmed = False
        self.refunded = False
        
    @abstractmethod
    def confirm_payment(self):
        pass
    def refund_payment(self):
        pass
    def payment_receipt(self):
        pass
    def pay_in_installments(self):
        pass
    
class Credit(Payment):
    def __init__(self, value: float):
        super().__init__(value)
    
    def confirm_payment(self):
        self.confirmed = True 
        self.payment_date = datetime.now()
        return ("Pagamento confirmado!")
        
    def refund_payment(self):
        '''caso o pagamento não seja aceito (não foi confirmado), o estorno será feito imediatamente'''
        if not self.confirmed:
            return ("Pagamento não confirmado.")
        if self.refunded:
            return ("Pagamento já estornado.")
        '''no caso de ser apenas um estorno'''
        self.refunded = True
        return ("Pagamento estornado com sucesso!")
        
    def payment_receipt(self):
        return(
            "--- RECIBO ---\n"
            f"Valor: {self.value}\n"
            f"Data: {self.payment_date}\n"
            "Status: Confirmado"
        )
        
    def pay_in_installments(self, installments=2):
        if installments<1:
            return ("Número de parcelas inválido.")
        value_per_installments = self.value / installments
        return (f"{installments}x de {value_per_installments} no cartão.")

class Debit(Payment):
    def __init__(self, value: float):
        super().__init__(value)
    
    def confirm_payment(self):
        self.confirmed = True
        return ("Pagamento confirmado!")
    def refund_payment(self):
        if not self.confirmed:
            return ("Pagamento não confirmado.")
        if self.refunded:
            return ("Pagamento já estornado.")
        self.refunded = True
        return ("Pagamento estornado com sucesso!")
    def payment_receipt(self):
        return(
            "--- RECIBO ---\n"
            f"Valor: {self.value}\n"
            f"Data: {self.payment_date}\n"
            "Status: Confirmado"
        )

class Pix(Payment):
    def __init__(self, value: float, pix_key: str):
        super().__init__(value)
        self._pix_key = pix_key
    
    def confirm_payment(self):
        self.confirmed = True
        return("Pagamento confirmado!")
    def refund_payment(self):
        if not self.confirmed:
            return("Pagamento não confirmado.")
        if self.refunded:
            return("Pagamento já estornado.")
        self.refunded = True
        return("Pagamento estornado com sucesso!")
    def payment_receipt(self):
        return(
            "--- RECIBO ---\n"
            f"Valor: {self.value}\n"
            f"Data: {self.payment_date}\n"
            "Status: Confirmado"
        )

class Cash(Payment):
    def __init__(self, value: float):
        super().__init__(value)
    
    def confirm_payment(self):
        self.confirmed = True
    def refund_payment(self):
        if not self.confirmed:
            return("Pagamento não confirmado.")
        if self.refunded:
            return("Pagamento já estornado.")
    def calculate_change(self, paid_value):
        return paid_value - self.value
  
class Order:
    def __init__(self, order_num: int): 
        self._order_num = order_num
    #retorna os dados do pedido dentro de um dicionario, pra gente poder passar pro json e criar o pedido dentro do json    
    def dic_order(self, email, num_order, name_product, distance):
        return{
            "email": email,
            "num_order": num_order,
            "name_product": name_product,
            "distance": distance,
            "status": "on hold" #em espera, ou seja aguardando o gerente aceitar o pedido, para que possa dar procedencia
        }  
    def create(self, email, name_product, distance):
        orders = load_orders()
        new_order = self.dic_order(email, self._order_num, name_product, distance)
        orders.append(new_order)
        save_orders(orders)
        print(f"Pedido efetuado: {new_order}")
    #verificar esse update, ja que essa funcao vai ser mt importante pras demais coisas, pra atualizar status etc
    def update(self, update_data: dict):
        code = ["num_order"]
        update_json(update_data, code)
        print(f"Pedido {update_data.get('num_order')} atualizado.")
    def delete(self):
        orders = load_orders()
        orders = [order for order in orders if order.get("num_order") != self._order_num]
        save_orders(orders)
        print(f"Pedido {self._order_num} deletado.")