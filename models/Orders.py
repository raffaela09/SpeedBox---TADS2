from random import randint
class Order:
    def __init__(self, email_client, code, product, address_client):
        self._email_client = email_client
        self._code = self.random_code()
        self._product = product
        self._address_client = address_client
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
        
    '''Funcao para gerar um numero aleatório com 4 algarismos, para isso foi utilizada a biblioteca Random, e para gerar o numero, utilizei randint, passando de 1000 a 9999, para assim gerar o codigo com 4 algarismos'''
    @staticmethod #por nao usar self, nem algum atributo de objeto, sendo assim, utilizamos staticmethod
    def random_code():
        code = randint(1000, 9999)
        return code
    '''Para mostrar uma mensagem ao usuario (cliente) ao concluir seu pedido'''
    @staticmethod #por nao usar self, nem algum atributo de objeto, sendo assim, utilizamos staticmethod
    def message_code(code):
        print(f"Order placed successfully! Order code: {code}")
        
    def data_order_dic(self):
        return {
            'client': self.email_client,
            'code': self.code,
            'product': self.product,
            'address_client': self.address_client
        }
        
# code = Order.random_code()        
# Order.mensage_code(code)
