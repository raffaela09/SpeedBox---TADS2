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

    def view_delivery_history(email):
        orders = load_orders()
        #here it goes through the emails to find orders
        his_order = [order for order in orders if order.get("email") == email]

        if not his_order:
            raise ValueError("You dont have delivery history.")
        else:
            for i, order in enumerate(his_order, start=1):
                items = ", ".join(order.get("items", []))
                status = order.get("status", "Unknown")
                print(f"\nOrder {i}")
                print(f"Items : {items}")
                print(f"Status: {status}")
