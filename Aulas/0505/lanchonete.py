#O que define um item do cardápio: nome, descrição e preço
#O que precisa exibir: nome, descrição e preço

class ItemCardapio:
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
    
    def getnome(self):
        return self.nome
    
    def getdescricao(self):
        return self.descricao

    def getpreco(self):
        return self.preco

    def setnome(self, nvnome):
        self.nome = nvnome

    def setdescricao(self, nvdescricao):
        self.descricao = nvdescricao

    def setpreco(self, nvpreco):
        self.preco = nvpreco

    def exibir_detalhes(self):
        print (self.nome, ' - ', self.descricao, ' - R$', self.preco)
    
class Cliente:
    def __init__(self, nome, numero, endereco): #Precisa de self.numero e self.endeco no atributo?
        self.nome = nome
        self.numero = numero
        self.endereco = endereco

    def getnome(self):
        return self.nome
    
    def getnumero(self):
        return self.numero

    def getendereco(self):
        return self.endereco

    def setnome(self, nvnome):
        self.nome = nvnome

    def setnumero(self, nvnumero):
        self.numero = nvnumero

    def setendereco(self, nvendereco):
        self.endereco = nvendereco

    def exibir_detalhes(self):
        print (self.nome, ' - ', self.numero, ' - ', self.endereco)

class Pedido():
    def __init__(self, cliente): #É assim mesmo?
        self.cliente = cliente
        self.itens_pedido = []
        self.status = "Aberto"

    def adicionar_item(self, item): #Verificar se existe no cardápior geral
        itens_pedido.append(item)

    def calcular_total(self):
        for i in itens_pedido:
            total += i.getpreco()
        return total

    def exibir_resumo(self):
        self.cliente.exibir_detalhes()
        for i in itens_pedido:
            print(i.getnome(), ' - ', i.getpreco())
        print(calcular_total())
        print('Status: ', self.status) 
        
    def finalizar_pedido(self):
        self.status = 'Finalizado'

cardapio_lanchonete = []

xburger = ItemCardapio('X-Burger', 'Pão, queijo, picles, cebola, alface, carne', 15.00)
batatafrita = ItemCardapio('Batata frita', 'Batata, sal', 18.00)
refrigerantelata = ItemCardapio('Refrigerante', 'Lata, 300ml, Coca-Cola', 6.00)
suconatural = ItemCardapio('Suco', 'Natural, laranja, 200ml, com açúcar', 9.00)

cardapio_lanchonete = [xburger, batatafrita, refrigerantelata, suconatural]

cliente1 = Cliente('Otávio', '(11)95587-3268', 'Rua Itinguçu, 1500')
    
pedido1 = Pedido(cliente1)

print('Escolha um item do cardápio')
for x in cardapio_lanchonete:
    print(x)

while(True)
    escolha = input("O que deseja: (para finalizar pedido, digite 1)")
    if escolha = '1':
        break
    elif escolha in cardapio_lanchonete:
        pedido1.adicionar_item(escolha) 
    else: 
        print("Esse produto não está no cardápio") 

pedido1.exibir_resumo()
pedido1.finalizar_pedido()
pedido1.exibir_resumo()

#Cliente está sendo utilizado para fornecer alguns dados que são exibidos em exibir_resumo
#Item_cardapio fornece dados de 




