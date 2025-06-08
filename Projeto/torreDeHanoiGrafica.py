pino1 = ['-------', ' -----', '  ---', '   -']
pino2 = []
pino3 = []
jogadas = 0

def verificar(pinoO, pinoD):
    if not pinoD:
        pinoD.append(pinoO[-1])
        del pinoO[-1]
    elif pinoO[-1] < pinoD[-1]:
        pinoD.append(pinoO[-1])
        del pinoO[-1]
    else:
        print("O disco movido deve ser menor que o primeiro da torre de destino")

print("Vamos começar!\nO jogo é: Torre de Hanoi\nO objetivo é mover todos os discos para o terceiro pino")
print("Dê duas entradas em 'mover disco', o número da torre que possui o disco e o número da torre para o qual deseja movê-lo")
print('Para escolher a primeira torre, digite 1')
print('Para escolher a segunda torre, digite 2')
print('Para escolher a terceira torre, digite 3')

while(True):
    print('Torre 1')
    for i in reversed(pino1):
        print(i)
    print('*'*20)
    print('Torre 2')
    for i in reversed(pino2):
        print(i)
    print('*'*20)
    print('Torre 3')
    for i in reversed(pino3):
        print(i)

    print("Mover disco: ")
    origem, destino = map(int, input().split())
    jogadas += 1
    if origem == 1:
        if destino == 2:
            verificar(pino1, pino2)
        elif destino == 3:
                verificar(pino1, pino3)
        else: 
            print("Valor inválido")
    elif origem == 2:
        if destino == 1:
            verificar(pino2, pino1)
        elif destino == 3:
            verificar(pino2, pino3)
        else: 
            print("Valor inválido")
    elif origem == 3:
        if destino == 2:
            verificar(pino3, pino2)
        elif destino == 1:
            verificar(pino3, pino1)
        else: 
            print("Valor inválido")
    else:
        print("número inválido")

    if pino3 == [4, 3, 2, 1]:
        print('Parabéns, você venceu!')
        print('Número de jogadas: ', jogadas)
        break