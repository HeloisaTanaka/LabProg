class Perfil:
    def __init__(self, id, nome):
        self._id = id
        self._nome = nome

    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def data(self):
        perfil = {
            'id': self.id,
            'nome': self.nome
        }
        return perfil

Perfis_lista = []

def createPerfil(id, nome):
    novoPerfil = Perfil(str(id), nome)
    Perfis_lista.append(novoPerfil)

def searchPerfilById(id):
    for perfil in Perfis_lista:
        if perfil.id == id:
            return perfil.data
    return False

def searchPerfilByNome(nome):  
    for perfil in Perfis_lista:
        if perfil.nome == nome:
            return perfil.data
    return False

def updatePerfil(id, novoNome):
    for perfil in Perfis_lista:
        if perfil.id == id:
            perfil._nome == novoNome
            return True
    return False

def deletePerfil(id):
    for perfil in Perfis_lista:
        if perfil.id == id:
            Perfis_lista.remove(perfil)
            return True
    return False
