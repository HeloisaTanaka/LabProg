class Produto:
    def __init__(self, id, nome, preco):
        self._id = id
        self._nome = nome
        self._preco = preco

    def setNome(self, novoNome):
        self._nome = novoNome

    def setPreco(self, novoPreco):
        self._preco = novoPreco
    
    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def preco(self):
        return self._preco
    
    