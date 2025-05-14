import json #pretendo usar no login
import uuid

class Person:
    def __init__(self, name: str, cpf: str):
        self._name = name
        self.__cpf = cpf # Private because it's sensitive content  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value): 
        self._name = value

    @property
    def _cpf(self):
        return self.__cpf

    @_cpf.setter
    def _cpf(self, value):
        self.__cpf = value

    # Takes no arguments

class User(Person):
    def __init__(self, name: str, cpf: str, email: str, pwd: str, user_type: str):
        super().__init__(name, cpf) 
        self.__id = str(uuid.uuid4())[:4] # Retrieves only the first 4 characters of the UUID
        self._email = email # Attributes are protected to support inheritance
        self.__pwd = pwd# Private attribute due to sensitive content
        self._user_type = user_type 

    @property
    def id(self):
        return self.__id 

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def _pwd(self):
        return self.__pwd

    @_pwd.setter
    def _pwd(self, value):
        self.__pwd = value

    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, value):
        self._user_type = value

    def login(self): #talvez usar json 
        pass
    
    def create_account(self):
        pass

    def view_delivery_history(self):
        pass

    def verify_pwd(self, pwd):
        return self.__pwd == pwd #checking if the entered password is equal to the stored password

class Client(User):
    def __init__(self, name: str, cpf: str, email: str, pwd: str, user_type: str, phone: int):
       super().__init__(name, cpf, email, pwd, user_type)
       self.__id = str(uuid.uuid4())[:4]
       self._phone = phone

    @property
    def __id(self): # ID generated via UUID, encapsulated with read-only access
        return self.__id 

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    def request_delivery(self):
        pass

    def receive_delivery(self):
        if self.status == "On route":
            self.status = "Delivered"

    def cancel_order(self):
        if self.status == "canceled":
            print("Order already canceled.")
        else:
            self.status = "Cancel"
            print("Order canceled successfully.")