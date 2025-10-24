from models.users import Users

class Hospedes:
    def __init__(self, id, nome, cpf, phone, email, id_user):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._email = email
        if phone:
            self._phone = phone
        if id_user:
            for user in Users:
                if user.id_user_sistema == id_user:
                    self._id_user = id_user

    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def email(self):
        return self._email
    
    @property
    def phone(self):
        if hasattr(self, '_phone'):
            return self._phone
        return 'Nenhum telefone registrado'
    
    @property
    def id_user(self):
        if hasattr(self, '_id_user'):
            return self._id_user
        return 'Este hóspede não possui id no sistema'
    
    @property
    def dados(self):
        hospede = {
            'id': self._id,
            'nome': self._nome,
            'cpf': self._cpf,
            'email': self._email
        }

        if hasattr(self, '_phone'):
            hospede['telefone'] = self._phone
        if hasattr(self, '_id_user'):
            hospede['Id_user_sistema'] = self._id_user

        return hospede


Hospedes_lista = []

def verificarDuplicidade(novoHospede):
    for hospede in Hospedes_lista:
        if hospede.cpf == novoHospede.cpf or hospede.nome == novoHospede.nome:
            return False
    return True

################################ CRUD
def addHospede(novoHospede):
    if verificarDuplicidade(novoHospede):
        Hospedes_lista.append(novoHospede)
        return True
    return False

def alterHospede(cpf, campo, valor):
    for hospede in Hospedes_lista:
        if hospede.cpf == cpf:
            if campo == '_phone':
                if hasattr(hospede, '_phone'):
                    setattr(hospede, campo, valor)
            elif campo == '_id_user':
                if hasattr(hospede, '_id_user'):
                    setattr(hospede, campo, valor)
            else:
                setattr(hospede, campo, valor)
            return True
    return False

def dellHospede(cpf):
    for hospede in Hospedes_lista:
        if hospede.cpf == cpf:
            Hospedes_lista.remove(hospede)
            return True
    return False

def searchHospedeByName(nome):
    for hospede in Hospedes_lista:
        if hospede.nome == nome:
            return hospede.dados
    return False