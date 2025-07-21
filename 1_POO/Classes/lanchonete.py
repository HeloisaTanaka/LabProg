#Exercício cujo objetivo é criar um programa para registrar pedidos, exibindo os 
#dados do cliente (nome, telefone, enedereço) e as informações do pedido (produtos,
#quantidades, preço total, status). O programa deve permitir que o usuário 
#verifique o pedido, finalize-o ou cancele-o.

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
        print ( 'INFORMAÇÕES DO(S) PRODUTO(S)' ,'\nProduto: ', self.nome, '\nDescrição: ', self.descricao, '\nPreço: R$', self.preco)
    
class Cliente:
    def __init__(self, nome, numero, endereco): 
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
        print ('\nDADOS DO CLIENTE', '\nNome: ', self.nome, '\nTelefone: ', self.numero, '\nEndereço: ', self.endereco)

class Pedido():
    def __init__(self, cliente): 
        self.cliente = cliente
        self.itens_pedido = []
        self.status = "Aberto"
        self.total = 0
    
    def getItens(self):
        return self.itens_pedido
    def adicionar_item(self, item):
        self.itens_pedido.append([item, 1])

    def setquantidade(self, item):
        for i in self.itens_pedido:
            if i[0] == item:
                i[1] += 1

    def calc_total(self, item):
        self.total += item

    def exibir_resumo(self):
        self.cliente.exibir_detalhes()
        print('\nINFORMAÇÕES DO PRODUTO:')
        for i in self.itens_pedido:
            print(i[1], i[0].getnome(), ' - ', i[0].getpreco()*i[1])
        print('Total: ', self.total)
        print('Status: ', self.status) 
        
    def finalizar_pedido(self):
        self.status = 'Finalizado'

xburger = ItemCardapio('X-Burger', 'Pão, queijo, picles, cebola, alface, carne', 15.00)
batatafrita = ItemCardapio('Batata frita', 'Batata, sal', 18.00)
refrigerantelata = ItemCardapio('Refrigerante', 'Lata, 300ml, Coca-Cola', 6.00)
suconatural = ItemCardapio('Suco', 'Natural, laranja, 200ml, com açúcar', 9.00)

cardapio_lanchonete = [xburger, batatafrita, refrigerantelata, suconatural]

cliente1 = Cliente('Otávio', '(11)95587-3268', 'Rua Itinguçu, 1500')
pedido1 = Pedido(cliente1)

print('Escolha um item do cardapio')
for x in cardapio_lanchonete:
    print(x.getnome(), ' - ', x.getpreco())

print('Digite o nome do produto que deseja para adicioná-lo ao seu pedido.')
print('Digite 1 para verificar seu pedido\nDigite 2 para finalizar o pedido\nDigite 3 para cancelar o pedido')
while(True):
    escolha = input("O que deseja: (para finalizar o pedido, digite 1)")
    if escolha == '1':
        pedido1.exibir_resumo()
    elif escolha == '2':
        pedido1.finalizar_pedido()
        pedido1.exibir_resumo()
        print('Agradecemos a preferência, volte sempre!')
        break
    elif escolha == '3':
        print('Pedido cancelado')
        break
    else:
        change = False
        for item in cardapio_lanchonete: 
            if item.getnome() == escolha:
                adc = False
                for i in pedido1.getItens():
                    if i[0] == item:
                        pedido1.setquantidade(i[0])
                        adc = True
                if not adc:
                    pedido1.adicionar_item(item)
                change = True
                pedido1.calc_total(item.getpreco()) 
        if not change:
            print('Este item não existe')




