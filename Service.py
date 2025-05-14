import os 
import json
from Exceptions import ProductNotFoundError

class Service:
    def __init__(self, folder, file_json):
        self._folder = folder
        self._file_json = file_json
        
    @property
    def folder(self):
        return self._folder
    @folder.setter
    def folder(self, value):
        self._folder = value
        
    @property 
    def file_json(self):
        return self._file_json
    @file_json.setter
    def file_json(self, value):
        self._file_json = value
#----------------------------------------------------------    

    def get_path(self):
        return os.path.join(self._folder, self._file_json)
    
    '''carrega os dados do json''' 
    def load_data(self):
        file_path = self.get_path()
        #verifica se o arquivo json existe e se ele nao esta vazio
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, 'r') as file:
                return json.load(file)
        else:
           return []
    #----------------------------------------------------------    
    
        
    def save_data(self, data_dict):
        '''Salva os dados do json'''
        data = self.load_data()
        data.append(data_dict)
        
        #caminho da pasta e nome do arquivo
        file_path = self.get_path()
        
        #cria e salva os dados dentro do json
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            
    def update_data(self, update_dict, keys):
        '''funcao para atualizar algum dado, atualiza somente um item no json, com base nas chaves (keys)'''
        data = self.load_data()
        found = False
        
        for item in data:
            match = True
            
            for key in keys:
                if item.get(key) != update_dict.get(key):
                    match = False
                    break
            if match:
                item.update(update_dict)
                found = True
                break
        if not found:
            raise ProductNotFoundError('Item nao encontrado.')
            
        with open(self.get_path(), 'w') as file:
            json.dump(data, file, indent=4)
            
    def product_details(self, item):
        '''Metodo para mostrar os detalhes do produto'''
        print(f'\nProduto: {item['product']}\nCódigo do produto: {item['code']}\nDestino: {item['destination']}\nStatus: {item['status']}\n')