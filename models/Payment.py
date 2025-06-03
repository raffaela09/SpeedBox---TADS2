from datetime import datetime
from abc import ABC, abstractmethod
#nome de arquivos que sao de classes comeca com letrar maiusculas ok, se for fazer comentario no codigo, descreve bem e usa docstring as tres aspas la
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
    
class Credit(Payment):
    def confirm_payment(self, value: float):
        self.value = value
        self.confirmed = True
        self.payment_date = datetime.now()
        
    def refund_payment(self):
        '''caso o pagamento não seja aceito (não foi confirmado), o estorno será feito imediatamente'''
        if not self.confirmed:
            return ("Pagamento não confirmado.")
        if self.refunded:
            return ("Pagamento já estornado.")
        '''no caso de ser apenas estorno'''
        self.refunded = True 
        return ("Pagamento estornado com sucesso.")
    def payment_receipt(self):
        return(
            "--- RECIBO ---\n"
            f"Valor: {self.value}\n"
            f"Data: {self.payment_date}\n"
            "Status: Confirmado"
        ) 
    def pay_in_installments(self, installments = 2):
        if installments < 1:
            return ("Número de parcelas inválido")
        else:
            value_per_installments = self.value / installments
            return ("{installments}x de {value_per_installments} no cartão.")
    def payment_dict(self):
        return {
            'method': 'credit',
            'value': self.value,
            'status': 'awaiting'
        }

class Debit(Payment):
    def confirm_payment(self, value: float):
        self.value = value
        self.confirmed = True
        self.payment_date = datetime.now()
        
    def refund_payment(self):
        if not self.confirmed:
            return ("Pagamento não confirmado.")
        if self.refunded:
            return ("Pagamento já estornado.")
            self.refunded = True
            return("Pagamento estornado com sucesso.")
    def payment_receipt(self):
        return(
            "--- RECIBO ---\n"
            f"Valor: {self.value}\n"
            f"Data: {self.payment_date}\n"
            "Status: Confirmado"
        ) 
    def payment_dict(self):
        return {
            'method': 'debit',
            'value': self.value,
            'status': 'awaiting'
        }

class Pix(Payment):
    def __init__(self, value: float):

        self.value = value
        self.confirmed = True
        self.payment_date = datetime.now()
        
    def confirm_payment(self):
        self.confirmed = True
        return ("Pagamento confirmado.")
    def refund_payment(self):
        if not self.consssfirmed:
            return ("Pagamento não confirmado.")
        if self.refunded:
            return ("Pagamento já estornado.")
        self.refunded = True 
        return ("Pagamento estornado com sucesso.")
    def payment_receipt(self):
        return(
            "--- RECIBO ---\n"
            f"Valor: {self.value}\n"
            f"Data: {self.payment_date}\n"
            "Status: Confirmado"
        ) 
    def payment_dict(self):
        return {
            'method': 'pix',
            'value': self.value,
            'status': 'awaiting'
        }

class Cash(Payment):
    def confirm_payment(self):
        self.confirmed = True 
        return ("Pagamento confirmado.")
    def refund_payment(self):
        if not self.confirmed:
            return ("Pagamento não confirmado.")
        if self.refunded:
            return ("Pagamento já estornado.")
        self.refunded = True 
        return ("Pagamento estornado com sucesso.") 
    def calculate_change(self):
        pass
    def payment_dict(self):
        return {
            'method': 'cash',
            'value': self.value,
            'status': 'awaiting'
        }