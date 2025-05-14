from Service import Service
from Exceptions import ProductNotFoundError

class ManagerBusiness:
    def __init__(self):
        pass
    def schedule_delivery():
        ...
    def refuse_delivery():
        ...
    def evaluate_delivery():
        ...
        
#aqui nesse caso herda do service, mas posso mudaar isso
class BusinessManager(Service):
    def __init__(self, folder, file_json):
        super().__init__(folder, file_json) 
        
    def accept_order(self, code):
         self.change_status(
           code = code,
           status = 'Em espera',
           status_alterado = 'Pronto para entrega',
           mensagem = f'O pedido {code} foi aceito e está aguardando coleta.',
           error = ProductNotFoundError,
           msg_error = 'Nenhum produto com esse código encontrado.'
           
       )
         
    def reject_order(self, code):
        self.change_status(
           code = code,
           status = 'Em espera',
           status_alterado = 'Cancelado',
           mensagem = f'O pedido {code} foi cancelado pela loja.',
           error = ProductNotFoundError,
           msg_error = 'Nenhum produto com esse código encontrado.'
           
       )