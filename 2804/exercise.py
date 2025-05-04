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
    
    def atualizar_Q(self, nova_quantidade):
        self.nova_quantidade = nova_quantidade
        self.quantidade = nova_quantidade
        return self.nova_quantidade

Produto1 = Produto('Melancia', 20.00, 50)
print('Valor do produto: ', Produto1.calcular_VT())
print('Quantidade do prouto: ', Produto1.atualizar_Q(55))
