class UsuarioModel:
    _usuarios = [{'id': 1, 'nome': 'Ana Silva', 'email': 'ana@email.com', 'senha': '2345'},
                 {'id': 2, 'nome': 'Bruno Costa', 'email': 'bruno@email.com', 'senha': '2345'}]
    _next_id = 3

    def get_todos(self):
        return self._usuarios
    
    def get_um(self, user_id):
        for user in self._usuarios:
            if user['id'] == user_id:
                return user
            return None
        
    def salvar(self, nome, email, senha):
        novo_usuario = {'id': self._next_id, 'nome': nome , 'email': email, 'senha': senha}
        self._usuarios.append(novo_usuario)
        self._next_id += 1
        return novo_usuario