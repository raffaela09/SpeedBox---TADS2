import openrouteservice #precisa ser baixado, por ser uma biblioteca, mas a gente passa isso no requirements.txt
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
    #------------------------------------------------------------    
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
    api_key = "5b3ce3597851110001cf6248bc7c0fcca0904e64afd670a881b44ec5"

    client = openrouteservice.Client(key = api_key)
    # nao da a rota exata, no caso as coordenadas, mesmo passando o numero, e centralizando a busca dentro da cidade, mesmo assim, pode dar em outra cidade, mas em ruas e avenidas mais famosas ele passa bem proximo
    #entao cabe ressaltar, que nao é uma estimativa EXATA, é apenas uma ESTIMATIVA, de quantos km sao e quanto tempo duraria
    #numeros sao pouco considerados, ou geralmente ignorados
    #é interessante ressaltar que ele faz a busca com base na popularidade dentro da cidade
    #ruas que sao comuns, ou existem em diversas cidades, pode fazer com que resulte em resultados diferentes, dando em cidades diferentes, ou em outros lugares diferente do que foi passado
    #o pelias search faz o auto complet, de bairro pra que possa fazer a busca, e se baseia no mais famoso, entao ao fazer a busca, deve-se passar o bairro junto.
    def geocode(self, address):
        full_address = f"{address}, Três Lagoas, MS, Brasil" # forcei a busca somente dentro da cidade, ou seja, aqui ele digita a rua somente, e aqui pega o endereco completo
        result = self.client.pelias_search(
            text=full_address,
            country='BR'
        ) # ele vai buscar pelo pelias, com base no endereco e o pais, forcando mais uma vez a busca 
        coords = result['features'][0]['geometry']['coordinates'] #aqui ele passa as coordenadas, mas se vc for testar, ele ta invertido, entao jogando no maps, tem que passar invertido ta
        return coords
    #------------------------------------------------------------

#fazer o requirements.txt e adicionar no readme

   
    #dividir isso aqui em dois metodos, um calcula o tempo e outro a distancia.
    def distance_time(self, pickup, destination, transport):
    #ja com directions é possivel fazer o calculo que precisamento, ou seja, o geo é um caminho que 
    #precisamos seguir para conseguir a distancia e a duração
        route = self.client.directions(
            coordinates=[pickup, destination],
            profile= transport.type_transport(), #passar isso aqui com base no transporte escolhido pelo entregador, mexer nas classes pra retornar pro 
            format='geojson'
        )

        summary = route['features'][0]['properties']['summary']
        distance = summary.get('distance', 0) / 1000  # km
        duration = summary.get('duration', 0) / 60  # min

        return distance, duration
    #------------------------------------------------------------
