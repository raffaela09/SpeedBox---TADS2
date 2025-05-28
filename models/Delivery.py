class Delivery:
    def __init__(self, addres_client, address_manager, address_delivery_man):
        self.__address_client = addres_client
        self.__address_manager = address_manager
        self.__address_delivery_man = address_delivery_man
        
    @property
    def address_client(self):
        return self.__address_client
    @address_client.setter
    def address_client(self, value):
        self.__address_client = value
        
    @property
    def address_manager(self):
        return self.__address_manager
    @address_manager.setter
    def address_manager(self, value):
        self.__address_manager = value
    
    @property
    def address_delivery_man(self):
        return self.__address_delivery_man
    @address_delivery_man
    def address_delivery_man(self, value):
        self.__address_delivery_man = value