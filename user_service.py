import bcrypt
from save_json import load_users,  save_users
#from speedBox_izab3lla import User

class User_service:
    def login(email: str, pwd:str): 
            users = load_users() # Loading the list of existing users from the JSON
            
            for user in users: # Iterate through the saved JSON data
                if user ["email"] == email:
                    hashed_pwd = user["pwd"].encode('utf-8') # Pega o hash da senha armazenada e codifica para bytes
                    if bcrypt.checkpw(pwd.encode('utf-8'), hashed_pwd): #Compara a senha digitada
                            return
                    else:
                        raise ValueError("Incorrect password")
                else:
                    raise ValueError("Email not found. please register")
                        
    def create_account(user_dict):
        users = load_users()  #carrega todos os usuarios que estao dentro do json
        users.append(user_dict)# Adds the user to the list
        save_users(users) # Saves to the JSON file 
        print("Registration successful!")
