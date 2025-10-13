from models.Produto import Produto

class Produtos:
    def __init__(self):
        self.produtos = []
        pass

    def getProdutos(self):
        return self.produtos

    def adicionar(self, novoProd): #novoProd é da classe Produto
        self.produtos.append(novoProd)

    def excluir(self, id_prod):
        found = False
        for prod in self.produtos:
            if prod.id == int(id_prod):
                found = True
                self.produtos.remove(prod)
        if not found:
            return 'Produto não encontrado'
    
    def getProd(self, id_prod):
        found = False
        for prod in self.produtos:
            if prod.id == int(id_prod):
                found = True
                return prod
        if not found:
            return False
                
        