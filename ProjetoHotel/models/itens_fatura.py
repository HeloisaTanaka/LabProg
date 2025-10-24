class Item_fatura:
    def __init__(self, id, id_fatura, id_servico, quantidade, preco_unitario, data_consumo):
        self._id = id
        self._fatura = id_fatura
        self._servico = id_servico
        self._quantidade = quantidade
        self._preco = preco_unitario
        self._consumo = data_consumo

    @property
    def id(self):
        return self._id
    
    @property
    def fatura(self):
        return self._fatura
    
    @property
    def servico(self):
        return self._servico
    
    @property
    def quantidade(self):
        return self._quantidade
    
    @property
    def preco(self):
        return self._preco
    
    @property
    def consumo(self):
        return self._consumo
    
    @property
    def data(self):
        item = {
            'id': self.id,
            'id_fatura': self.fatura,
            'id_servico': self.servico,
            'quantidade': self.quantidade,
            'preco_unitario': self.preco,
            'data_consumo': self.consumo
        }
        return item
    
Itens_fatura_lista = []

def createItem(id, id_fatura, id_servico, quantidade, preco_unitario, data_consumo):
    item = Item_fatura(str(id), str(id_fatura), str(id_servico), quantidade, preco_unitario, data_consumo)
    Itens_fatura_lista.append(item)

def searchItem(id):
    for item in Itens_fatura_lista:
        if item.id == id:
            return item.data
    return False

def updateItem(id, campo, valor):
    for item in Itens_fatura_lista:
        if item.id == id:
            setattr(item, campo, valor)
            return True
    return False

def deleteItem(id):
    for item in Itens_fatura_lista:
        if item.id == id:
            Itens_fatura_lista.remove(item)
            return True
    return False