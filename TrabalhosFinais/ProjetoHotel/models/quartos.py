#aplicar validações
"""def validacaoGeral(tipo, capacidade, diariaBase, descricao, numero, statusLimpeza, localização):
    validacoes = [(validarTipo(tipo), 'Tipo inválido'), 
                  (validarCapacidade(capacidade), 'Capacidade inválida'),
                  (validarDiaria(diariaBase), 'Diária inválida')]
    
    if descricao:
        validacoes.append((validarDescricao(), 'Descrição inválida'))
    
    erros = []
    for validacao, mensagem in validacoes:
        if not validacao:
            erros.append(mensagem)
    
    if erros:
        raise ValueError(erros)
    return True

def validarTipo(tipo):
    if not tipo:
        return False"""
  
class Quartos:
    def __init__(self, id, tipo, capacidade, diariaBase, descricao, numero, statusLimpeza, localizacao):
    
        self._id = id
        self._tipo = tipo
        self._capacidade = capacidade
        self._diariaBase = diariaBase
        self._numero = numero
        self._statusLimpeza = statusLimpeza
        self._localizacao = localizacao
        if descricao:
            self._descricao = descricao

    @property
    def id(self):
        return self._id

    @property
    def tipo(self):
        return self._tipo

    @property
    def capacidade(self):
        return self._capacidade

    @property
    def diaria(self):
        return self._diariaBase

    @property
    def numero(self):
        return self._numero

    @property
    def sttLimpeza(self):
        return self._statusLimpeza

    @property
    def localizacao(self):
        return self._localizacao

    @property
    def descricao(self):
        if hasattr(self, 'descricao'):
            return self._descricao
        return None

    @property
    def data(self):
        room = {
            'id': self.id,
            'tipo': self.tipo,
            'capacidade': self.capacidade,
            'diaria': self.diaria,
            'numero': self.numero,
            'sttLimpeza': self.sttLimpeza,
            'localizacao': self.localizacao,
            'descricao': self.descricao
        }
        return room


###################### CRUD
Rooms_list = []

def addRoom(newRoom):
    Rooms_list.append(newRoom)

def deleteRoom(id):
    for room in Rooms_list:
        if room.id == id:
            Rooms_list.remove(room)
            return True
    return False

def updateRoom(id, campo, valor):
    for room in Rooms_list:
        if room.id == id:
            setattr(room, campo, valor)
            return True
    return False

def searchRoomById(id):
    for room in Rooms_list:
        if room.id == id:
            return room.data
    return False

