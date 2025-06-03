from services.Service import Service
from models.Exceptions import PasswordOrEmailInvalidError
import bcrypt

class UserService(Service):
    def __init__(self, name_file):
        super().__init__(name_file)
        
    def login(self, email, pwd): 
        users = self.load_data() # Loading the list of existing users from the JSON
        print(users)
        for user in users: # Iterate through the saved JSON data
            if user ["email"] == email:
                hashed_pwd = user["pwd"].encode('utf-8') # Pega o hash da senha armazenada e codifica para bytes
                if bcrypt.checkpw(pwd.encode('utf-8'), hashed_pwd): #Compara a senha digitada
                        print(f"\nEmail confirmed! Welcome {user["name"].upper()}!\n")
                        return user 
        raise PasswordOrEmailInvalidError("\nIncorrect e-mail or password!")
            
    def create_account(self, user_dict):
        users = self.load_data()  #carrega todos os usuarios que estao dentro do json
        users.append(user_dict)# Adds the user to the list
        self.save_data(users) # Saves to the JSON file 
        print("\nRegistration successful!\n")