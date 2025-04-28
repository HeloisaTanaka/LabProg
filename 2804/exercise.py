#Crie uma classe chamada Produto
#atributos: nome, preço, quantidade
#métodos: calcular valor total(preço * quantidade)
#método: recebe o parâmetro nova quantidade de produtos e atualiza a quantidade de produtos no atributo quantidade

#Crie alguns objetos do tipo produto, calcule seus valores totais e atualize a quantidade de cada um deles

class Produto:
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preco = preço
        self.quantidade = quantidade

    def calcular_VT(self):
        return self.preco * self.quantidade
    
    def 

