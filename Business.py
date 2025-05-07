class Business:
    def __init__(self, cnpj):
        self._cnpj = cnpj
        
    @property
    def cnpj(self):
        return self._cnpj
    @cnpj.setter
    def cpnj(self, value):
        self._cnpj = value