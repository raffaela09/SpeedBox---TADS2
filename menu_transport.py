from speedBox_Julia import Motorcyle, Car, Bicycle

def main():
    vehicle = None 
    
    while vehicle is None: # enquanto o value do transporte for inválido
        transport = input("Which transport would you like? (Car/Motorcycle/Bicycle)\n").strip().lower()
        
        if transport == "motorcycle":
            vehicle = Motorcyle("DEF456", 1, 80) # instancia da classe 
        
        elif transport == "car":
            vehicle = Car("ABC123", 1.5, 60)
            
        elif transport == "bicycle":
            vehicle = Bicycle(0.5, 20)
        
        else:
            print("That's not a valid transport option. Please choose Car, Motorcycle or Bicycle.")
            
    distance = float(input("Enter the distance em km: "))
    time = vehicle.estimated_time(distance)
    minutes = time * 60
    delivery_price = vehicle.total_price(distance)
    print(f"Estimated delivery time: {minutes} minutes")
    print(f"Total delivery price: {delivery_price} reais")
    
main()
    