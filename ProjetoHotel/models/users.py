import re

class User:
    def __init__(self, id, nome, email, senha, confirmar, perfil):
        if validacao_geral(nome, email, senha, confirmar, perfil):
            self._id = id
            self._nome = nome
            self._email = email
            self._senha = senha
            self._perfil = perfil

    @property
    def id_user_sistema(self):
        return self._id

    @property
    def nome(self):
        return self._nome
    
    @property
    def email(self):
        return self._email
    
    @property 
    def senha(self):
        return self._senha
    
    @property
    def perfil(self):
        return self._perfil
    
    @property
    def user_dados(self):
        user = {
            'id': self._id,
            'nome': self._nome,
            'email': self._email,
            'perfil': self._perfil
        }
        return user
    
    def alterarSenha(self, novaSenha):
        if validarSenha(novaSenha):
            self._senha = novaSenha
        else: raise ValueError('Nova senha inválida')

    def alterarNome(self, novoNome):
        if validarNome(novoNome):
            self._nome = novoNome
        else: raise ValueError('Novo nome inválido')
        
    def alterarEmail(self, novoEmail):
        if validarEmail(novoEmail):
            self._email = novoEmail
        else: raise ValueError('Novo email inválido')

    def alterarPerfil(self, novoPerfil):
        if validarPerfil(novoPerfil):
            self._perfil = novoPerfil
        else: raise ValueError('Novo perfil inválido')

################################################## VALIDAÇÕES

def validacao_geral(nome, email, senha, confirmar, perfil):
    validacoes = [(validarNome(nome), 'Nome inválido'),
                 (validarEmail(email), 'Email inválido'),
                 (validarSenha(senha, confirmar), 'Senha inválida'),
                 (validarPerfil(perfil), 'Perfil inválido')]
    erros = []
    for validade, mensagem in validacoes:
        if validade == False:
            erros.append(mensagem)
        
    if erros:
        raise ValueError(erros)
    return True
    
def validarNome(nome):
    if not nome:
        return False
    if not isinstance(nome, str) or len(nome)<5 or len(nome)>100:
        return False
    pattern = r'^[a-zA-ZÀ-ÿ]+$'
    return bool(re.match(pattern, nome.strip()))

def validarEmail(email):
    if not email:
        return False
    if not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-z]{2,}$'
    return bool(re.match(pattern, email))

def validarSenha(senha, confirmar):
    if not senha or not confirmar:
        return False
    if len(senha)<8:
        return False
    if not re.search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)', senha):
        return False
    return senha == confirmar

def validarPerfil(perfil):
    if not perfil:
        return False
    perfils = ['1', '2', '3', '4']
    if not perfil in perfils:
        return False
    return True

################################################## USERS

Users_lista = []

def verificarDuplicidade(novoUser):
    for user in Users_lista:
        if user.nome == novoUser.nome or user.email == novoUser.email:
            return False
    return True

def verificarLogin(email, senha):
    for usuario in Users_lista:
        if usuario.email == email:
            if usuario.senha == senha:
                return True
            return 'Senha incorreta'
    return 'Usuário não encontrado'

############################# CRUD

def addUser(novoUser):
    if verificarDuplicidade(novoUser):
        Users_lista.append(novoUser)
        return True
    raise ValueError('Usuário já existe')

def alterUser(id, dado, valor):
    for user in Users_lista:
        if user.id_user_sistema == id:
            setattr(user, dado, valor)
            return True
    return False

def dellUser(id):
    for user in Users_lista:
        if user.id_user_sistema == id:
            Users_lista.remove(user)
            return True
    return False

def searchUserById(valor):
    for user in Users_lista:
        if user.id_user_sistema == valor:
            return user.user_dados
    return False

def searchUserByEmail(valor):
    for user in Users_lista:
        if user.email == valor:
            return user.user_dados
    return False

    


            