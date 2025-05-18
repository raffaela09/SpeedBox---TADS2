import json
 
# Implementing JSON to save the user
def load_users():#loads the existing users
    try:
        with open("users.json", "r") as file:
            return json.load(file) 
    except FileNotFoundError:
        return [] 

#salva na lista e joga dentro do json "users.json" com o dump
def save_users(users): #saves in a list
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)
        