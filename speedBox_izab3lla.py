import uuid
from services.service import load_orders, load_users, save_users, save_orders
import bcrypt
from models.Exceptions import PasswordInvalidError, CodeAlreadyExisitError
#separa em arquivos de classes, tipo arquivo de pessoa, arquivo de user, etc
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
        users = load_users() # Loading the list of existing users from the JSON

        for user in users: # Iterate through the saved JSON data
            if user ["email"] == email:
                    hashed_pwd = user["pwd"].encode('utf-8') # Pega o hash da senha armazenada e codifica para bytes
                    if bcrypt.checkpw(pwd.encode('utf-8'), hashed_pwd): #Compara a senha digitada
                        print(f"Email confirmed! Welcome {user["name"].upper()}!")
                        return user 
                    else:
                        raise PasswordInvalidError("Incorrect password")

    def create_account(user_dict):
        users = load_users()  #carrega todos os usuarios que estao dentro do json
        users.append(user_dict)# Adds the user to the list
        save_users(users) # Saves to the JSON file 
        print("Registration successful!")

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
        orders = load_orders()
        existing_codes = [order["num_order"] for order in orders]
        if place_order["num_order"] in existing_codes:
            raise CodeAlreadyExisitError("Order code already exists. Please use a unique code.")
        #adiciona tambem ao atributo da classe (order), que faz parte da associacao
        self.order.append(place_order)

        #adiciona o pedido a lista que é retornada do load_user
        orders.append(place_order)
        #salva os pedidos no json
        save_orders(orders)
        #retorna uma msg pro usuario
        print("Order created and saved, awaiting for answer.")
     

    # def receive_delivery(self):
    #     received_confirmation = received()
    #     if self.status == "on route": # Checks if the status is "on route"
    #         if received_confirmation:# if so, confirms it
    #             print("Order delivered!") # Otherwise, the status will be "confirmed"
    #     else:
    #         print("Order canceled!")

    # def cancel_order(self):
    #     confirm = cancel_input()  # calling function created in the inputs page
    #     if self.status == "canceled":  # check if the order has already been canceled
    #         print("Order already canceled.")
    #     elif confirm:
    #         self.status = "canceled"  # if not canceled, confirm and cancel the order
    #         print("Order canceled successfully.")