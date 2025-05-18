import bcrypt
from save_json import load_users,  save_users
from speedBox_izab3lla import User

class User_service:
    def login(email: str, pwd:str): 
            users = load_users() # Loading the list of existing users from the JSON
            
            for user in users: # Iterate through the saved JSON data
                if user ["email"] == email:
                    hashed_pwd = user["pwd"].encode('utf-8') #Gets the stored password hash and encodes it to bytes
                    if bcrypt.checkpw(pwd.encode('utf-8'), hashed_pwd): #Compares the entered password
                            return
                    else:
                        raise ValueError("Incorrect password")
                else:
                    raise ValueError("Email not found. please register")
                        
    def create_account(user_dict):
        users = load_users() #"Loads all users stored in the JSON file"
        users.append(user_dict)# Adds the user to the list
        save_users(users) # Saves to the JSON file 
        print("Registration successful!")
