from Exceptions import ProductNotFoundError
from speedBox_izab3lla import User
from save_json import load_orders, update_json
class ManagerBusiness(User):
    def __init__(self, name, cpf, email, pwd, user_type):
        super().__init__(name, cpf, email, pwd, user_type)
    #----------------------------------------------------------------------------------- 
    '''funcao responsável por aceitar um pedido, irá verificar de acordo com o código do pedido se está no json e com o status correto (nesse caso, status de em espera),
    caso esteja, ele chama a funcao de atualizar os dados do json, que passa o que vai ser atualizado e por qual chave ele deve procurar dentro do json para atulizar, caso contrario, ele levanta uma excecao.
    ''' 
    def schedule_delivery(self, num_order):
        orders = load_orders()
        for order in orders:
            if num_order == order["num_order"] and order["status"] == "on hold":
                update_json(
                    update_orders={
                        "num_order": num_order, 
                        "status": "awaiting pickup"
                    },
                    keys=["num_order"]
                )
            else:
                pass
    #-----------------------------------------------------------------------------------
    
    
    
    '''Funcao responsavel por cancelar um pedido, ela funciona da mesma forma que a anterior, verifica atravez do codigo do pedido se esta no json e com o status em espera, caso esteja, ele chama a funcao de atualizar os dados no json, que recebe os dados que vao ser
    atualizados e por qual chave deve-se procurar dentro do json para que possa ser atualizado, caso contrario, ele levanta uma excecao
    '''             
    def refuse_delivery(self, num_order):
        orders = load_orders()
        for order in orders:
            if num_order == order["num_order"] and order["status"] == "on hold":
                update_json(
                    update_orders={
                        "num_order": num_order, 
                        "status": "canceled"
                    },
                    keys=["num_order"]
                )
                break
        else:
            pass
    #-----------------------------------------------------------------------------------
            
    def evaluate_delivery():
        ...
        

