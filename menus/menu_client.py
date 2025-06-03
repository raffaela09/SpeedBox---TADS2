from models.Exceptions import CodeAlreadyExisitError, NoProductsToDisplayError
from services.OrderService import OrderService
from services.ClientService import ClientService
from models.Orders import Order
from models.Delivery import Delivery
from models.Payment import Cash, Credit, Debit, Pix

'''Funcao para escolher o pagamento, caso deseje pagar no app'''
def chose_payment(value):
    #recebe o valor do produto, como somos apenas o intermediario da entrega, deixei pro proprio usuario digitar o valor do produto
    #ver de colocar um while e opcao de sair do while
    print('\nChose your method:\n1 - Credit\n2 - Debit\n3 - Pix\n4 - Cash\n')
    chose_payment_input = input('Enter your option: ')
    if chose_payment_input == '1':
        return Credit(value)
    elif chose_payment_input == '2':
        return Debit(value)
    elif chose_payment_input == '3':
        return Pix(value)
    elif chose_payment_input == '4':
        return Cash(value)
    else:
        #arrumar isso
        print('Inválid option.')
        return None
        
def input_place_order():
    try:
        print("\n------- Place Order --------\n")
        product = input("Product: ").strip().lower()
        print("\nEnter just your street.\nExample: 'Rua Rayldo de Oliveira Gomes'")
        address_client = input('Enter your address: ').strip().lower()
        value_product_str = input('Enter the value of the order: ').strip()
        value_product_float = float(value_product_str)
        pay_on_delivery = input('Would you like to pay on delivery? Y/N').strip().lower()
        payment_method = chose_payment(value_product_float)
        return product, address_client, pay_on_delivery, value_product_float, payment_method
    #arruma esse erro aqui, pra fazer o raise em algum canto e subir o erro mas sem parar o codigo.
    except ValueError:
        print("Inválid input for value. Please enter a number.")
    
def create_order(client_email, product, address_client, payment_method):
    code = Order.random_code() #chama a funcao de gerar o código aleatório do pedido
    date_time = Order.date_time() #pra salvar a data e hora que o pedido foi feito
    delivery_teste = Delivery(address_client)
    addres_client_coords = delivery_teste.geocode(address_client)
    return Order(client_email, code, product, addres_client_coords, date_time, payment_method)

'''Funcao para fazer o pedido'''
def place_order(client, product, address_client, pay_on_delivery, payment_method):
    client_service = ClientService('orders.json')
    try:
        order = create_order(client.email, product, address_client, payment_method)
        if pay_on_delivery == 'y':
            client_service.request_delivery(order.data_order_dic())
            order.message_code()
        elif pay_on_delivery == 'n':
            client_service.request_delivery(order.data_order_dic())
            order.message_code()
        else:
            print('Inválid option for payment.')
            
    except CodeAlreadyExisitError as error:
        print(error) #passar outro erro, ja que agora o sistema que gera o codigo
#-------------------------------------

#mostrar as opcoes do cliente      
def options_user(client):
    order_service = OrderService("orders.json") 
    while True:
        print("1 - Place Order\n2 - Show history.\n3 - Logout.")
        answer_client = input("Enter your option: ")
        #cria o pedido
        if answer_client == "1":
            try:
                product, address_client, pay_on_delivery, value, payment_method = input_place_order()
                place_order(client, product, address_client, pay_on_delivery, payment_method)
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
        else:
            print('Inválid Option.')
#-------------------------------------