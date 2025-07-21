#Implemente uma versão onde o computador posiciona os seus navios secretamente 
#num tabuleiro de dimensões fixas (ex: 10x10). O usuário clica nas células do
#tabuleiro para tentar acertar os navios do computador. 
# O sistema informa se o tiro acertou na água, num navio ou afundou um navio. 
# O objetivo é afundar todos os navios do computador.

import random

tabuleiroUsuario = [[' ' for i in range(9)] for j in range(9)]
tabuleiroSecreto = [[' ' for i in range(9)] for j in range(9)]

def exibirTabuleiroUsuario():
    linha = 0
    print('    1 ', ' 2 ', ' 3 ', ' 4 ', ' 5 ', ' 6 ', ' 7 ', ' 8 ', ' 9 ')
    for i in tabuleiroUsuario:
        linha +=1
        print(' ','+---'*9+'+')
        print(linha, '|', " | ".join(i), '|')
    print(' ', '+---'*9+'+')

def posicionarNaviosV():
    z=0
    naviosV = []
    while z<=4:
        y = random.randint(0, 7)
        x = random.randint(0, 7)

        if tabuleiroSecreto[y][x] == ' ' and tabuleiroSecreto[y+1][x] == ' ':
            tabuleiroSecreto[y][x] = 'O'
            tabuleiroSecreto[y+1][x] = 'O'
        else:
            z-=1
        z+=1

        navio = [[y, x], [y+1, x]]
        naviosV.append(navio)
    return naviosV    
    
def posicionarNaviosH():
    z=0
    naviosH = []
    while z<=4:
        y = random.randint(0, 7)
        x = random.randint(0, 7)

        if tabuleiroSecreto[y][x] == ' ' and tabuleiroSecreto[y][x+1] == ' ':
            tabuleiroSecreto[y][x] = 'O'
            tabuleiroSecreto[y][x+1] = 'O'
        else:
            z-=1
        z+=1

        navio = [[y, x], [y, x+1]]
        naviosH.append(navio)
    return naviosH    

def afundar(navios):
    valor = 0
    for i in navios:
        if tabuleiroUsuario[navios[valor][0][0]][navios[valor][0][1]] == 'O' and tabuleiroUsuario[navios[valor][1][0]][navios[valor][1][1]] == 'O':
            tabuleiroUsuario[navios[valor][0][0]][navios[valor][0][1]] = 'X'
            tabuleiroUsuario[navios[valor][1][0]][navios[valor][1][1]] = 'X'
            exibirTabuleiroUsuario()
            del navios[valor]
            print('Você afundou um navio!')
        valor+=1

def jogo():
    count = 0
    for i in tabuleiroUsuario:
        for j in i:
            if j == 'X':
                count+= 1
    if count == 20:
        print('Parabéns, você afundou todos os navios!')
        return False
    else:
        return True
       
print("Vamos começar! O jogo é Batalha Naval!")
print("Você deve digitar dois números separados por espaço.")
print("Eles serão suas coordenadas:\nO primeiro número representa a linha\nO segundo número representa a coluna do tabuleiro")
print("O = navio atingido")
print("X = navio afundado")
print("~ = água atingida")
print("Que comece o jogo!\n")

exibirTabuleiroUsuario()
naviosV = posicionarNaviosV()
naviosH = posicionarNaviosH()
acertos = []
jogada = []
game = True

while(game):
    palpiteX, palpiteY = map(int, input("Coordenada: ").split())
    if tabuleiroSecreto[palpiteX-1][palpiteY-1] == 'O':

        tabuleiroUsuario[palpiteX-1][palpiteY-1] = 'O'
        afundar(naviosV)
        afundar(naviosH)
        
        if not tabuleiroUsuario[palpiteX-1][palpiteY-1] == 'X':
            exibirTabuleiroUsuario()
            print('Você atingiu um navio')

    else:
        tabuleiroUsuario[palpiteX-1][palpiteY-1] = '~'
        exibirTabuleiroUsuario()
        print('Nenhum navio nessa coordenada')

    game = jogo()






       


