from models.Exceptions import ItemNotFoundError
import json 

'''Classe de servico para facilitar a manutencao e manipulacao de dados do json'''
class Service:   
    def __init__(self, name_file):
        self._name_file = name_file
        
    @property
    def name_file(self):
        return self._name_file
    @name_file.setter
    def name_file(self, value):
        self._name_file = value
            
    '''metodo para carregar os dados dentro do json, basta passar o nome do arquivo que deseja carregar, nesse caso, ou orders, ou user'''  
    def load_data(self):
        try:
            with open(self._name_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    '''Metodo para salvar dados dentro do json, passa o dados que deseja salvar, e o nome do arquivo no qual vai salvar'''   
    def save_data(self, data):        
        with open(self._name_file, "w") as file:
            json.dump(data, file, indent=4) 
            
    '''Metodo para fazer atualizacao dos dados de dentro do json, sem que duplique o item que está lá dentro,
    verifico pra cada item dentro do json, se TODAS (por isso o All, funcao que vai me retornar true ou false, pra cada elemento,
    se todos forem verdadeiras, ou seja iguais, ele cai nessa validacao.
    ), 
    '''
    def update_json(self, update_data, keys):
        #utilizar esse json update para poder trocar de senha
        data = self.load_data()
        found = False 
        
        for item in data:
            if all(item[key] == update_data[key] for key in keys):
                item.update(update_data)
                found = True
                break
            
        if not found:
            raise ItemNotFoundError("Item not found.")
        self.save_data(data)
   
    '''deletar dados de dentro do json, ele verifica de acordo com o id (email, ou codigo do pedido) se o item possuir o "id"
    igual, ele adiciona a uma nova lista, e depois salva com o metodo "save_data", dessa forma, tirando o item que desejava excluir.
    '''   
    def delete_data(self, type_id, id_user):
        data = self.load_data()
        new_data = []
        for item in data:
            if item[type_id] != id_user:
                new_data.append(item)
        self.save_data(new_data)
