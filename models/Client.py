from models.User import User
        
class Client(User):
    def __init__(self, name: str, cpf: str, email: str, pwd: str, user_type: str):
       super().__init__(name, cpf, email, pwd, user_type)

