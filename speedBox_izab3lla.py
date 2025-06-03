import uuid
from services.Service import Service
import bcrypt
from models.Exceptions import PasswordOrEmailInvalidError
Service_User = Service("users.json")
Service_orders = Service("orders.json")
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

    def login(email, pwd): 
        users = Service_User.load_data() # Loading the list of existing users from the JSON

        for user in users: # Iterate through the saved JSON data
            if user ["email"] == email:
                    hashed_pwd = user["pwd"].encode('utf-8') # Pega o hash da senha armazenada e codifica para bytes
                    if bcrypt.checkpw(pwd.encode('utf-8'), hashed_pwd): #Compara a senha digitada
                        print(f"\nEmail confirmed! Welcome {user["name"].upper()}!\n")
                        return user 
            else:
                raise PasswordOrEmailInvalidError("\nIncorrect e-mail or password!")

    def create_account(user_dict):
        users = Service_User.load_data()  #carrega todos os usuarios que estao dentro do json
        users.append(user_dict)# Adds the user to the list
        Service_User.save_data(users) # Saves to the JSON file 
        print("\nRegistration successful!\n")

    def user_dic(self, name, cpf, email, pwd, user_type): #creating the dictionary for the json
      return {
          "name": name,
          "cpf": cpf,
          "email": email,
          "pwd": pwd,
          "type_user": user_type
      }  
        
class Client(User):
    def __init__(self, name: str, cpf: str, email: str, pwd: str, user_type: str, orders=None):
       super().__init__(name, cpf, email, pwd, user_type)
       self.order = [] #associacao de pedidos 

    def request_delivery(self, place_order):
        #carrega o historico global de pedidos, deve retornar uma lista
        orders = Service_orders.load_data()
        #adiciona tambem ao atributo da classe (order), que faz parte da associacao
        self.order.append(place_order)

        #adiciona o pedido a lista que é retornada do load_user
        orders.append(place_order)
        #salva os pedidos no json, utilizando da classe Service
        Service_orders.save_data(orders)
