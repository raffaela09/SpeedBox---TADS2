from speedBox_Julia import Order
from speedBox_izab3lla import Client

def menu_order():
    while True:
        print("--- MENU PEDIDOS ---")   
        print("1. Fazer pedido")
        print("2. Ataualizar pedido")
        print("3. Deletar pedido")
        print("4. Sair")
        
        order_option = input("Escolha uma opção: ")    
        
        if order_option == "1":
            num_order = int(input("Numero do pedido: "))
            email = input("E-mail do cliente: ")
            nome_produto = input("Nome do produto: ")
            distance = float(input("Distância em km: "))
            
            order = Order(num_order) 
            order.create(email, nome_produto, distance)
            
        elif order_option == "2":
            num_order = int(input("Número do pedido para atualizar: "))
            new_status = input("Novo status: ")
            
            order = Order(num_order) 
            order.update({"num_order": num_order, "status": new_status})
            
        elif order_option == "3":
            num_order = int(input("Núemro do pedido para deletar: "))
            
            order = Order(num_order)
            order.delete()
            
        elif order_option == "4":
            print("Encerrando.")
            break
        else:
            print("Opção inválida.")
                    
menu_order()