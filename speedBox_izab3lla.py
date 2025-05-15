import uuid
from save_json import load_users, save_users
from inputs_user import login_user, register_user, cancel_input, place_order, received

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

    def login(self, email, pwd): 
        users = load_users() # Loading the list of existing users from the JSON
        email, pwd = login_user() # Using inputs from another file

        for user in users: # Iterate through the saved JSON data
            if user ["email"] == email:
                if user ["pwd"] == pwd:
                    print("Email confirmed!")
                else:
                    print("Email not found. Please register.")

    def create_account(self, name, cpf, email, pwd):
        users = load_users() 
        name, cpf, email, pwd = register_user()

        if email in users: # Checks if the email exists and has already been registered
            print("Email already registered")
            return 
        
        new_user = User(name, cpf, email, pwd) # If the above condition is not met, it registers the new user
        users.append(new_user)# Adds the user to the list
        save_users(users) # Saves to the JSON file
        print("Registration successful!")

    def view_delivery_history(self):
        pass

    def verify_pwd(self, pwd):
      pass#checking if the entered password is equal to the stored password
    

class Client(User):
    def __init__(self, name: str, cpf: str, email: str, pwd: str, user_type: str, phone: int):
       super().__init__(name, cpf, email, pwd, user_type)
       self.__id = str(uuid.uuid4())[:4]
       self._phone = phone

    @property
    def __id(self): #ID generated via UUID, encapsulated with read-only access
        return self.__id 

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    def request_delivery(self):
        response = place_order()
        if response:
            self.status = "Order confirmed!"

    def receive_delivery(self):
        received_confirmation = received()
        if self.status == "on route":
            if received_confirmation:
                print("Order delivered!")
        else:
            print("Order canceled!")

    def cancel_order(self):
        confirm = cancel_input()  # calling function created in the inputs page
        if self.status == "canceled":  # check if the order has already been canceled
            print("Order already canceled.")
        elif confirm:
            self.status = "canceled"  # if not canceled, confirm and cancel the order
            print("Order canceled successfully.")