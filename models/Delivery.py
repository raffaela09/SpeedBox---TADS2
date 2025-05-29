import openrouteservice #precisa ser baixado, é uma biblioteca
class Delivery:
    def __init__(self, addres_client):
        '''Aqui consome a api, sendo exatamente a chave dela'''

        self.__address_client = addres_client

    
    @property
    def address_client(self):
        return self.__address_client
    @address_client.setter
    def address_client(self, value):
        self.__address_client = value
        
    # @property
    # def address_manager(self):
    #     return self.__address_manager
    # @address_manager.setter
    # def address_manager(self, value):
    #     self.__address_manager = value
    
    # @property
    # def address_delivery_man(self):
    #     return self.__address_delivery_man
    # @address_delivery_man
    # def address_delivery_man(self, value):
    #     self.__address_delivery_man = value
    
    
#o geo recebe os endereços como av. Olinto Mancini e transforma ela em coordenadas
#de longitude e latitude, acredito que é o melhor jeito visto que ninguem sabe as coordenadas de casa
#mas sim o endereço

#estuda bem essa bomba desse geocode pra ele n zerar isso aq
#passar pra ser somente na cidade, fazer try except, adicionar o resultado no json, pra que a gente possa fazer o calculo, 
#fazer a maquina gerar o codigo, terminar os try except,
#separar em classes de servico e organizar essa estrutura.
#fazer o requirements.txt e adicionar no readme

    def geocode(self, address, client = openrouteservice.Client(key = "5b3ce3597851110001cf6248bc7c0fcca0904e64afd670a881b44ec5")):
        full_address = f"{address}, Três Lagoas, MS, Brasil"
        result = client.pelias_search(text=full_address)
        coords = result['features'][0]['geometry']['coordinates']
        print(coords)
        return coords

    def distance_time(self, pickup, destination):
        pickup_coords = self.geocode(pickup)
        destination_coords = self.geocode(destination)

    #ja com directions é possivel fazer o calculo que precisamento, ou seja, o geo é um caminho que 
    #precisamos seguir para conseguir a distancia e a duração
        route = self.client.directions(
            coordinates=[pickup_coords, destination_coords],
            profile='driving-car', #passar isso aqui com base no transporte escolhido pelo entregador 
            format='geojson'
        )

        summary = route['features'][0]['properties']['summary']
        distance = summary['distance'] / 1000  # km
        duration = summary['duration'] / 60  # min

        return distance, duration
