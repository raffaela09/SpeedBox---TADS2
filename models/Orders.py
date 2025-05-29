from random import randint
class Order:
    def __init__(self):
        pass
    
    '''Funcao para gerar um numero aleatório com 4 algarismos, para isso foi utilizada a biblioteca Random, e para gerar o numero, utilizei randint, passando de 1000 a 9999, para assim gerar o codigo com 4 algarismos'''
    def random_code():
        code = randint(1000, 9999)
        return code
    
    