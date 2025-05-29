from models.Exceptions import CodeAlreadyExisitError, NoProductsToDisplayError
from services.OrderService import OrderService
from models.Orders import Order
from models.Delivery import Delivery
#fazer pedido
def place_order(client):
    try:
        print("\n------- Place Order --------")
        #inputs do cliente
        product = input("Product: ")
        print("Enter your street and house number:\nExample: 'Rua Rayldo de Oliveira Gomes, 1079'")
        addres_client = input("Enter address: ")
        #----------------------------
        
        code = Order.random_code()
        date_time = Order.date_time()
        
        #criacao das instancias da classe
        delivery_teste = Delivery(addres_client)
        addres_client_coords = delivery_teste.geocode(addres_client)
        order = Order(client.email, code, product, addres_client_coords, date_time)
        #----------------------------
        
        date_dic_order = order.data_order_dic()
        client.request_delivery(date_dic_order)
        Order.message_code(code)
    except CodeAlreadyExisitError as error:
        print(error) #passar outro erro, ja que agora o sistema que gera o codigo
#-------------------------------------

#mostrar as opcoes do 
#opcoes do usuario, como cliente       
def options_user(client):
    order_service = OrderService("orders.json")
    
    while True:
        print("1 - Place Order\n2 - Show history.\n3 - Logout.")
        answer_client = input("Enter your option: ")
        #cria o pedido
        if answer_client == "1":
            try:
                place_order(client)
            except NoProductsToDisplayError as error:
                print(error)
        #para ver historico de pedidos
        elif answer_client == "2":
            try:
                order_service.show_history(type_user = client.user_type, email_user = client.email)
            except NoProductsToDisplayError as error:
                print(error)
        #para sair
        elif answer_client == "3":
            print('See you soon!')
            break
#-------------------------------------