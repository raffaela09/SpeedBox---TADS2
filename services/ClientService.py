from services.Service import Service
class ClientService(Service):
    def __init__(self, name_file):
        super().__init__(name_file)
        
    def request_delivery(self, place_order):
        #carrega o historico global de pedidos, deve retornar uma lista
        orders = self.load_data()
        #adiciona tambem ao atributo da classe (order), que faz parte da associacao

        #adiciona o pedido a lista que é retornada do load_user
        orders.append(place_order)
        #salva os pedidos no json, utilizando da classe Service
        self.save_data(orders)