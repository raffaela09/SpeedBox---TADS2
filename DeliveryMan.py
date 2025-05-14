from Service import Service
from Exceptions import ProductNotFoundError
class DeliveryMan:
    def __init__(self):
        pass
    def make_delivery():
        ...
    def collect_delivery():
        ...
        

class DeliveryManManager(Service):
    def __init__(self, folder, file_json):
        super().__init__(folder, file_json)
                     
    def pick_up_order(self, code):
       self.change_status(
           code = code,
           status = 'Pronto para entrega',
           status_alterado = 'Em rota para entrega',
           mensagem = f'O pedido {code} foi aceito e está em rota para entrega.',
           error = ProductNotFoundError,
           msg_error = 'Nenhum produto com esse código encontrado.'
           
       )
        
    def deliver_order(self, code):
        self.change_status(
            code = code,
            status = 'Em rota para entrega',
            status_alterado = 'Pedido entregue.',
            mensagem = f'O pedido {code} foi entrego e pago com sucesso!',
            error = ProductNotFoundError,
            msg_error = 'Nenhum produto com esse código encontrado.'
        )
    
    def show_history_delivery(self):
        orders = self.load_data()
        orders_route = []
        orders_finally = []
        
        if orders:
            for order in orders:
                if order['status'] == 'Pedido em rota para entrega':
                    orders_route.append(order)
                if order['status'] == 'Pedido entregue':
                    orders_finally.append(order)
        if orders_route:
            print('Pedidos em rota pra entrega:\n')
            for item in orders_route:
                self.product_details(item)
        if orders_finally:
            print('Pedidos finalizados:\n')
            for item in orders_finally:
                self.product_details(item)            
        if not orders_finally and not orders_route:
            raise ProductNotFoundError('Nenhum pedido encontrado.')