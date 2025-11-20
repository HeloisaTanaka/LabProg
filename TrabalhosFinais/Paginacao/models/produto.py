from .db import db

class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    @classmethod
    def adicionar(cls, nome, preco):
        novoProd = cls(nome=nome, preco=preco)
        db.session.add(novoProd)
        db.session.commit()

    def excluir(self):
        db.session.delete(self)
        db.session.commit()

    def alterar(self, nome, preco):
        self.nome = nome
        self.preco = preco
        db.session.commit()



    


