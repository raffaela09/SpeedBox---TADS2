import json

def user_dic(self): #creating the dictionary for the json
      return {
          "id": self.__id,
          "name": self._name,
          "cpf": self.__cpf,
          "email": self._email,
          "pwd": self.__pwd,
      }  
    
# Implementing JSON to save the user
def load_users():#loads the existing users
    try:
        with open("users.json", "r") as file:
            return json.load(file) 
    except FileNotFoundError:
        return [] 

def save_users(users): #saves in a list
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)