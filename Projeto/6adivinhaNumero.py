import random

numero = random.randint(1, 100)
count = 0

print('Vamos começar! Você deve adivinhar um número aleatório de 1 a 100')
while(True):
    count += 1
    tentativa = int(input('Palpite: '))
    if tentativa == numero:
        print('Parabéns, você ganhou')
        print('Número de tentativas: ', count)
        break
    elif numero-tentativa <= -30:
        print('Tentativa muito alta')
    elif numero-tentativa <= -15:
        print('Tentativa um pouco alta')
    elif numero-tentativa >= 30:
        print('Tentativa muito baixa')
    elif numero-tentativa >= 15:
        print('Tentativa um pouco baixa')
    else:
        if tentativa > numero:
            print('Chegou perto! tente um pouco mais baixo')
        else:
            print('Chegou perto! tente um pouco mais alto')