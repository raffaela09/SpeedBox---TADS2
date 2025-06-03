from random import randint
import datetime
from models.Payment import Payment
class Order:
    def __init__(self, email_client, code, product, address_client, date_and_time, payment = None):
        self._email_client = email_client
        self._code = self.random_code()
        self._product = product
        self._address_client = address_client
        self._date_and_time = self.date_time()
        self._payment = payment
    #---------------------------------- 
    
    #propertys
    @property
    def email_client(self):
        return self._email_client
    @email_client.setter
    def email_client(self, value):
        self._email_client = value
    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, value):
        self._code = value
    @property
    def product(self):
        return self._product
    @product.setter
    def product(self, value):
        self._product = value
    @property
    def address_client(self):
        return self._address_client
    @address_client.setter
    def address_client(self, value):
        self._address_client = value
    @property
    def date_and_time(self):
        return self._date_and_time
    @date_and_time.setter
    def date_and_time(self, value):
        self._date_and_time = value
    @property
    def payment(self):
        return self._payment
    @payment.setter
    def payment(self, value):
        self._payment = value
    #---------------------------------- 
     
    '''Funcao para gerar um numero aleatório com 4 algarismos, para isso foi utilizada a biblioteca Random, e para gerar o numero, utilizei randint, passando de 1000 a 9999, para assim gerar o codigo com 4 algarismos'''
    @staticmethod #por nao usar self, nem algum atributo de objeto, sendo assim, utilizamos staticmethod
    def random_code():
        code = randint(1000, 9999)
        return code
    #---------------------------------- 
    
    '''Para mostrar uma mensagem ao usuario (cliente) ao concluir seu pedido'''
     #por nao usar self, nem algum atributo de objeto, sendo assim, utilizamos staticmethod
    def message_code(self):
        print(f"Order placed successfully!\nOrder code: {self.code}")
    #---------------------------------- 
    
    '''Funcao para pegar a data e hora do momento, para que possa armazenar no pedido, utilizei a classe datetime, e formatei a data para uma string'''
    @staticmethod
    def date_time():
        #pega a hora e a data atuais, ou seja, do exato momento em que o pedido foi efetuado
        now = datetime.datetime.now()
        #strftime (formatador de tempo em string) - (string format time ), ou seja ele vai formatar para ficar dia, mes, ano, hora, minutos e segundos, vindo da biblioteca date time, entao ele vai converter o objeto datetime em uma string formatada.
        formatad = now.strftime("%d/%m/%Y %H:%M:%S")
        return formatad
    #---------------------------------- 
    
    '''funcao para retornar os dados dentro de um dicionario, para que assim possa salvar dentro do json'''   
    def data_order_dic(self):
        return {
            'cliente': self.email_client,
            'code': self.code,
            'product': self.product,
            'address_client': self.address_client,
            'status' : 'on hold',
            'date_time': self.date_and_time,
    'payment': self.payment.payment_dict() if self.payment else {
        'status': 'pending',
        'method': None #nada foi escolhido ainda, portanto expressa ausencia de valor 
    }
        }
    #---------------------------------- 
