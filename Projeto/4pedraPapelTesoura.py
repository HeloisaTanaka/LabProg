#Desenvolva o clássico jogo onde o usuário escolhe entre Pedra, Papel ou Tesoura. 
# O computador fará a sua escolha aleatoriamente. 
# O sistema então determina e exibe o vencedor da rodada (usuário, computador ou empate) e, 
# opcionalmente, mantém um placar.

import random

jogadas = ['pedra', 'papel', 'tesoura']
scoreP = 0
scoreC = 0

print('O jogo da vez é pedra, papel ou tesoura')
print('A competição será entre você e o computado, numa melhor de 5')
print('Que comece o jogo!\n')

for i in range (5):
    jogada = jogadas[random.randint(0, 2)]
    jogadaP = input('Digite sua jogada: ').lower()
    if jogadaP == 'pedra':
        if jogada == 'pedra':
            print('Jogada do computador:', jogada)
            print('Empate')
        elif jogada == 'papel':
            print('Jogada do computador:', jogada)
            print('Derrota')
            scoreC += 1
        else:
            print('Jogada do computador:', jogada)
            print('Vitória')
            scoreP += 1
    elif jogadaP == 'papel':
        if jogada == 'papel':
            print('Jogada do computador:', jogada)
            print('Empate')
        elif jogada == 'tesoura':
            print('Jogada do computador:', jogada)
            print('Derrota')
            scoreC += 1
        else:
            print('Jogada do computador:', jogada)
            print('Vitória')
            scoreP += 1
    elif jogadaP == 'tesoura':
        if jogada == 'tesoura':
            print('Jogada do computador:', jogada)
            print('Empate')
        elif jogada == 'pedra':
            print('Jogada do computador:', jogada)
            print('Derrota')
            scoreC += 1
        else:
            print('Jogada do computador:', jogada)
            print('Vitória')
            scoreP += 1
    else:
        print('Jogada inválida')

if scoreP > scoreC:
    print('Parabéns, você venceu!')
    print('Sua pontuação:', scoreP)
    print('Pontuação do oponente:', scoreC)
else:
    print('Poxa, você perdeu')
    print('Sua pontuação:', scoreP)
    print('Pontuação do oponente:', scoreC)