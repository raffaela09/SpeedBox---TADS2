from abc import ABC, abstractmethod

class Transport(ABC):
    @staticmethod
    @abstractmethod
    def type_transport():
        pass
    
class Car(Transport):
    
    def type_transport(distance):
        return 'driving-car'
    
    
class Motorcycle(Transport):
    
    def type_transport(distance):
        return 'driving-car' #o directions nao possui a rota pra motos, entao utilizei a rota de carro, ja que na teoria sao parecidas
    
    
class Bicycle(Transport):
    
    def type_transport(distance):
        return 'cycling-regular' #isso retorna o profile do directions