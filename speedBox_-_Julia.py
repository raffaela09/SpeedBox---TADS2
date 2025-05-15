from abc import ABC, abstractmethod

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

class Transport(ABC):
    @abstractmethod
    def estimated_time(self, distance):
        pass
    
class Motorcyle(Transport):
    def __init__(self, license_plate: str, km: float, price_per_km: float, average_speed: float):
        self._license_plate = license_plate
        self.km = km
        self._price_per_km = price_per_km
        self.average_speed = average_speed
    
    def estimated_time(self, distance):
        pass

class Car(Transport):
    def __init__(self, license_plate: str, km: float, price_per_km: float, average_speed: float):
        self._license_plate = license_plate
        self.km = km
        self._price_per_km = price_per_km
        self.average_speed = average_speed
    
    def estimated_time(self, distance):
        pass

class Bicycle(Transport):
    def __init__(self, km: float, price_per_km: float, average_speed: float):
        self.km = km
        self._price_per_km = price_per_km
        self.average_speed = average_speed
    
    def estimated_time(self, distance):
        pass

class Merchandise:
    def __init__(self, weight: float, size: float, fragile: bool, package: str, delivery_status: str):
        self._weight = weight
        self._size = size 
        self._fragile = fragile
        self._package = package
        self._delivery_status = delivery_status
        
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

class Order:
    def __init__(self, order_num: int, pickup: str, price: float, method: Payment): 
        self._order_num = order_num
        self._pickup = pickup
        self._price = price 
        self._method = method

    def create(self):
        pass
    def read(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass