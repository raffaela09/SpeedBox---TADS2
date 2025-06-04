from models.User import User
from services.OrderService import OrderService
from models.Exceptions import ItemNotFoundError, ProductNotFoundError
class ManagerBusiness(User):
    def __init__(self, name, cpf, email, pwd, user_type):
        super().__init__(name, cpf, email, pwd, user_type)
    #----------------------------------------------------------------------------------- 
    '''funcao responsável por aceitar um pedido, irá verificar de acordo com o código do pedido se está no json e com o status correto (nesse caso, status de em espera),
    caso esteja, ele chama a funcao de atualizar os dados do json, que passa o que vai ser atualizado e por qual chave ele deve procurar dentro do json para atulizar, caso contrario, ele levanta uma excecao.
    ''' 
    def schedule_delivery(self, num_order, email, user_type, address_manager):
        order_service = OrderService("orders.json")
        order_service.change_status(
            number_order = num_order, 
            email_user = email,
            mensage_status_search = "on hold",
            mensage_status_update = "awaiting pickup",
            type_user_key = user_type
        )
        orders = order_service.load_data()
        for order in orders:
            if order['code'] == num_order:
                # order['estimated_time'] = transport.estimated_time(distance = order['distance'])
                order['address_manager'] = address_manager
                order["code"] = int(order["code"])
                order_service.update_json(order, ['code'])
                break 
        else:
                raise ItemNotFoundError(f"Order with code {num_order} not found.")
    #-----------------------------------------------------------------------------------
    
    '''Funcao responsavel por cancelar um pedido, ela funciona da mesma forma que a anterior, verifica atravez do codigo do pedido se esta no json e com o status em espera, caso esteja, ele chama a funcao de atualizar os dados no json, que recebe os dados que vao ser
    atualizados e por qual chave deve-se procurar dentro do json para que possa ser atualizado, caso contrario, ele levanta uma excecao
    '''    
    #arrumar isso aq
             
    def refuse_delivery(self, num_order, email, user_type):
        try:
            order_service = OrderService("orders.json")
            order_service.change_status(
                number_order = num_order,
                email_user = email,
                mensage_status_search = "on hold",
                mensage_status_update = "canceled",
                type_user_key = user_type
            )
            print('Order canceled.')
        except ProductNotFoundError as error:
            print(error)
    #-----------------------------------------------------------------------------------
            

        

