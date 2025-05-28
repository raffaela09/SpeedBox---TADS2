import json 

'''Classe de servico para facilitar a manutencao e manipulacao de dados do json'''
class Service:   
    '''metodo para carregar os dados dentro do json, basta passar o nome do arquivo que deseja carregar, nesse caso, ou orders, ou user'''  
    def load_data(self, name_file):
        try:
            with open(name_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
    '''Metodo para salvar dados dentro do json, passa o dados que deseja salvar, e o nome do arquivo no qual vai salvar'''   
    def save_data(self, name_file, data):        
        with open(name_file, "w") as file:
            json.dump(data, file, indent=4) 
            
    '''Metodo para fazer atualizacao dos dados de dentro do json, sem que duplique o item que está lá dentro,
    verifico pra cada item dentro do json, se TODAS (por isso o All, funcao que vai me retornar true ou false, pra cada elemento,
    se todos forem verdadeiras, ou seja iguais, ele cai nessa validacao.
    )
    '''
    def update_json(self, update_data, keys, name_file):
        data = self.load_data(name_file)
        found = False 
        
        for item in data:
            if all(item[key] == update_data[key] for key in keys):
                item.update(update_data)
                found = True
                break
            
        if not found:
            raise FileNotFoundError('File not found.')
        with open(name_file, "w") as file:
            json.dump(data, file, indent=4) 
   
    '''deletar dados de dentro do json '''   
    def delete_data():
        pass

