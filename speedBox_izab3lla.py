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

    #Takes no arguments

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

    def user_dic(self, name, cpf, email, pwd, user_type): #creating the dictionary for the json
        return {
            "name": name,
            "cpf": cpf,
            "email": email,
            "pwd": pwd,
            "type_user": user_type
        }  

    def view_delivery_history(self):
        pass
  
class Client(User):
    def __init__(self, name: str, cpf: str, email: str, pwd: str, user_type: str, phone: int):
       super().__init__(name, cpf, email, pwd, user_type)
       self._phone = phone

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value 

    def request_delivery(self, place_order):
        response = place_order
        if response: 
            self.status = "Order confirmed!"

    def receive_delivery(self, received):
        received_confirmation = received
        if self.status == "On route": # Checks if the status is "on route"
            if received_confirmation:# if so, confirms it
                print("Order delivered!") # Otherwise, the status will be "confirmed"
        else:
            print("Order canceled!")

    def cancel_order(self, cancel_input):
        confirm = cancel_input  # calling function created in the inputs page
        if self.status == "canceled":  # check if the order has already been canceled
            print("Order already canceled.")
        elif confirm:
            self.status = "canceled"  # if not canceled, confirm and cancel the order
            print("Order canceled successfully.") 