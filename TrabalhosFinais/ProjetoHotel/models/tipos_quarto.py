class Tipo_quarto:
    def __init__(self, id, nome, capacidade, diaria, descricao=''):
        self._id = id
        self._nome = nome
        self._capacidade = capacidade
        self._diaria = diaria
        self._descricao = descricao

    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def capacidade(self):
        return self._capacidade
    
    @property
    def diaria(self):
        return self._diaria
    
    @property
    def descrição(self):
        return self._descricao
    
    @property
    def data(self):
        tipo = {
            'id': self.id,
            'nome': self.nome,
            'capacidade': self.capacidade,
            'diaria': self.diaria,
            'descricao': self.descrição
        }
        return tipo
    
Tipos_quarto_lista = []

def createTipoQuarto(id, nome, capacidade, diaria, descricao=''):
    novoTipo = (str(id), nome, capacidade, diaria, descricao)
    Tipos_quarto_lista.append(novoTipo)

def searchTipoById(id):
    for tipo in Tipos_quarto_lista:
        if tipo.id == id:
            return tipo.data
    return False

def updateTipo(id, campo, valor):
    for tipo in Tipos_quarto_lista:
        if tipo.id == id:
            setattr(tipo, campo, valor)
            return True
    return False

def deleteTipo(id):
    for tipo in Tipos_quarto_lista:
        if tipo.id == id:
            Tipos_quarto_lista.remove(tipo)
            return True
    return False