'''classes abstratas'''
from abc import ABC, abstractmethod 
from datetime import datetime

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
    def  __init__(self, value: float):
        super().__init__(value)
        
    def confirm_payment(self):
        self.confirmed = True
        self.payment_date = datetime.now()
        return ("Pagamento confirmado!")
    
    def refund_payment(self):
        '''caso o pagamento não seja aceito (não foi confirmado), o estorno seerá feito imediatamente'''
        if not self.confirmed:
            return ("Pagamento não confirmado")
        if self.refunded:
            return ("Pagamento já estornado.")
        '''no caso de ser apenas um estorno'''
        self.refunded = True
        return ("Pagamento estornado com sucesso")
        
    def payment_receipt(self):
        return (
            "--- RECIBO ---\n"
            f"Valor: {self.value}\n"
            f"Data: {self.payment_date}\n"
            "Status: Confirmado"
        )
        
    def pay_in_installments(self, installments = 2):
        if installments < 1:
            return ("Número de parcelas inválido.")
        value_per_installments = self.value / installments
        return (f"{installments}x de {value_per_installments} no cartão.")

class Debit(Payment):
    def __init__(self, value: float):
        super().__init__(value)
                
    def confirm_payment(self):
        self.confirmed = True
        self.payment_date = datetime.now() 
        return ("Pagamento confirmado!")
            
    def refund_payment(self):
        if not self.confirmed:
            return ("Pagamento não confirmado.")
        if self.refunded:
            return ("Pagamento já estornado.")
        self.refunded = True
        return ("Pagamento estornado com sucesso!")
            
    def payment_receipt(self):
        return (
            "--- RECIBO ---\n"
            f"Valor: {self.value}\n"
            f"Data: {self.payment_date}\n"
            "Status: Confirmado"
        )
            
class Pix(Payment):
    def __init__(self, value: float, pix_key: str):
        super().__init__(value)
        self.__pix_key = pix_key
        
    @property
    def pix_key(self):
        return self.__pix_key
    
    @pix_key.setter
    def pix_key(self, value):
        self.__pix_key = value
        
    def confirm_payment(self):
        self.confirmed = True
        self.payment_date = datetime.now()
        return ("Pagamento confirmado!")
    
    def refund_payment(self):
        if not self.confirmed:
            return ("Pagamento não confirmado.")
        if self.refunded:
            return ("Pagamento já estornado.")
        self.refunded = True
        return ("Pagamento estornado com sucesso!")
    
    def payment_receipt(self):
        return (
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
        self.payment_date = datetime.now()
        return ("Pagamento confirmado!")
    
    def refund_payment(self):
        if not self.confirmed:
            return ("Pagamento não confirmado.")
        if self.refunded:
            return ("Pagamento já estornado.")
        self.refunded = True 
        return ("Pagamento estornado com sucesso!")
    
    def calculate_change(self, paid_value: float):
        return paid_value - self.value
    
    def payment_receipt(self):
        return (
                "--- RECIBO ---\n"
                f"Valor: {self.value}\n"
                f"Data: {self.payment_date}\n"
                "Status: Confirmado"
            )  
        