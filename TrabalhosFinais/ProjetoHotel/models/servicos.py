class Servico:
    def __init__(self, id, nome, preco):
        self._id = id
        self._nome = nome
        self._preco = preco

    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
    
    @property
    def data(self):
        servico = {
            'id': self.id,
            'nome': self.nome,
            'preco': self.preco
        }
        return servico
    
Servicos_lista = []

def createServico(id, nome, preco):
    novoServico = Servico(id, nome, preco)
    Servicos_lista.append(novoServico)

def searchServicoById(id):
    for servico in Servicos_lista:
        if servico.id == id:
            return servico.data
    return False

def updateServico(id, campo, valor):
    for servico in Servicos_lista:
        if servico.id == id:
            setattr(servico, campo, valor)
            return True
    return False

def deleteServico(id):
    for servico in Servicos_lista:
        if servico.id == id:
            Servicos_lista.remove(servico)
            return True
    return False
