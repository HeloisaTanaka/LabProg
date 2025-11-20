class Fatura:
    def __init__(self, id, id_reserva, data_emissao, valor_servicos, valor_diarias, stt_pagamento):
        self._id = id
        self._reserva = id_reserva
        self._emissao = data_emissao
        self._servicos = valor_servicos
        self._diarias = valor_diarias
        self._pagamento = stt_pagamento

    @property
    def id(self):
        return self._id
    
    @property
    def reserva(self):
        return self._reserva
    
    @property
    def emissao(self):
        return self._emissao
    
    @property
    def servicos(self):
        return self._servicos
    
    @property
    def diarias(self):
        return self._diarias
    
    @property
    def pagamento(self):
        return self._pagamento
    
    @property
    def data(self):
        reserva = {
            'id': self._id,
            'id_reserva': self._reserva,
            'data_emissao': self._emissao,
            'valor_servicos': self._servicos,
            'valor_diarias': self._diarias,
            'stt_pagamento': self._pagamento
        }
        return reserva
    
Faturas_lista = []

def addFatura(novaFatura):
    Faturas_lista.append(novaFatura)

def searchFaturaById(id):
    for fatura in Faturas_lista:
        if fatura.id == id:
            return fatura.data #Estou retornando um dicionário com os dados da fatura, não o obj
    return False

def updateFatura(id, campo, valor):
    for fatura in Faturas_lista:
        if fatura.id == id:
            setattr(fatura, campo, valor)
            return True
    return False

def deleteFatura(id):
    for fatura in Faturas_lista:
        if fatura.id == id:
            Faturas_lista.remove(fatura)
            return True
    return False
        