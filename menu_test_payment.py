from payment import Credit, Debit, Pix, Cash

def menu_payment():
    payment = None 
    
    while True:
        print("--- MENU DE PAGAMENTO ---")
        print("1. Forma de pagamento")
        print("2. Confirmar pagamento")
        print("3. Ver recibo")
        print("4. Estornar pagamento")
        print("5. Parcelar pagamento")
        print("6. Sair")
        option = input("Escolha uma opção: ")
        
        if option == "1":
            print("--- FORMA DE PAGAMENTO ---")
            print("a. Cartão de crédito")
            print("b. Cartão de débito")
            print("c. Pix")
            print("d. Em dinheiro")
            method = input("Escolha a forma do pagamento: ").lower()
            
            value = float(input("Valor da compra: "))
            
            if method == "a":
                payment = Credit(value)
            elif method == "b":
                payment = Debit(value)
            elif method == "c":
                pix_key = input("Pix key: ")
                payment = Pix(value, pix_key)
            elif method == "d":
                payment = Cash(value)
                paid_value = float(input("Valor pago pelo cliente: "))
                change = payment.calculate_change(paid_value)
                print(f"O troco é: {payment.calculate_change(paid_value)}")
            else: 
                print("Forma inválida.")
                
            print("Pagamento efetuado.")
        
        elif option == "2":
            if payment:
                print(payment.confirm_payment())
            else:
                print("Não há pagamento.")
            
        elif option == "3":
            if payment:
                print(payment.payment_receipt())
            else:
                print("Não há pagamento.")
                
        elif option == "4":
            if payment:
                print(payment.refund_payment())
            else:
                print("Não há pagamento.")
                
        elif option == "5":
            if payment:
                installments = int(input("Número de parcelas: "))
                print(payment.pay_in_installments(installments))
            else:
                print("Não há pagamento.")
                
        elif option == "6":
            print("Encerrando.")
            break
        else: 
            print("Opção inválida. Tente novamente.")
            
menu_payment()
    