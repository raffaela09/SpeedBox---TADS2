from abc import ABC, abstractmethod

class Delivery:
    def __init__(self, status: str, client, driver, pickup: str, destination: str, distance: int):
        self.__status = status 
        self.__client = client
        self.__driver = driver
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
        
    def calculate_estimated_time(self): # rever
        pass

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
    
    # dividir distancia por vel media, transformar em min
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
        self.__pix_key = pix_key
        
    @property
    def pix_key(self):
        return self.__pix_key
    
    @pix_key.setter
    def pix_key(self, value):
        self.__pix_key = value 
    
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

class Order:
    def __init__(self, order_num: int, pickup: str, price: float, payment_method: Payment): 
        self.__order_num = order_num
        self.__pickup = pickup
        self.__price = price 
        self.__payment_method = payment_method
        
    @property
    def order_num(self):
        return self.__order_num
    
    @order_num.setter
    def order_num(self, value):
        self.__order_num = value 
        
    @property
    def pickup(self):
        return self.__pickup
    
    @pickup.setter
    def pickup(self, value):
        self.__pickup = value 
        
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        self.__price = value 
        
    @property
    def payment_method(self):
        return self.__payment_method
    
    @payment_method.setter
    def payment_method(self, value):
        self.__payment_method = value 

    def create(self):
        pass
    def read(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass