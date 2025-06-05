class Pedido():
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens_pedido = []
        self.status = "Aberto"

    def adicionar_item(self, item):
        self.itens_pedido.append(item)  # Corrigido o uso do atributo da classe

    def calcular_total(self):
        total = 0  # Inicializando a variável total
        for i in self.itens_pedido:  # Correção: usar self.itens_pedido
            total += i.getpreco()
        return total

    def exibir_resumo(self):
        self.cliente.exibir_detalhes()
        for i in self.itens_pedido:
            print(i.getnome(), ' - ', i.getpreco())
        print("Total: R$", self.calcular_total())  # Chamar corretamente a função
        print('Status: ', self.status) 
        
    def finalizar_pedido(self):
        self.status = 'Finalizado'

# Criar cardápio
cardapio_lanchonete = [
    ItemCardapio('xburger', 'Pão, queijo, picles, cebola, alface, carne', 15.00),
    ItemCardapio('batatafrita', 'Batata, sal', 18.00),
    ItemCardapio('refrigerantelata', 'Lata, 300ml, Coca-Cola', 6.00),
    ItemCardapio('suconatural', 'Natural, laranja, 200ml, com açúcar', 9.00)
]

cliente1 = Cliente('Otávio', '(11)95587-3268', 'Rua Itinguçu, 1500')
pedido1 = Pedido(cliente1)

print('Escolha um item do cardápio:')
for item in cardapio_lanchonete:
    print(item.getnome(), ' - R$', item.getpreco())

while True:
    escolha = input("O que deseja? (Para finalizar pedido, digite 1) ")
    if escolha == '1':
        break
    else:
        # Verificar se o item existe no cardápio
        item_escolhido = next((item for item in cardapio_lanchonete if item.getnome() == escolha), None)
        if item_escolhido:
            pedido1.adicionar_item(item_escolhido)
        else:
            print("Esse produto não está no cardápio.") 

pedido1.exibir_resumo()
pedido1.finalizar_pedido()
pedido1.exibir_resumo()
