#Implemente o jogo da forca utilizando uma lista predefinida de palavras. 
# A cada rodada, uma palavra é escolhida aleatoriamente. 
# O usuário tenta adivinhar as letras. 
# A interface deve mostrar a palavra parcialmente descoberta, as letras já tentadas 
# (corretas e incorretas) e o número de tentativas restantes. 
# O usuário perde se cometer 6 erros.

import random

palavras = ['arbusto', 'serenata', 'amizade', ' inimigo', 'beijo', 'avestruz']
palavra = palavras[random.randint(0, 5)]
letras = []
erros = 0
nLetras = len(palavra)

def exibicao(letras, palavra):
    resultado = ''
    for i in palavra:
        if i in letras:
            resultado += i
        else:
            resultado += '_'
    return resultado

print("Vamos começar!")
print("Você deve adivinhar uma palavra, caso erre 6 letras ou acerte a palavra, o jogo termina")
print('_'*len(palavra))
print("Palavra com", nLetras, 'letras')

while(True):
    tentativa = input('Digite uma letra: ')
    letras.append(tentativa)
    if tentativa in palavra:
        print('Letra correta')
        print(exibicao(letras, palavra))
        if exibicao(letras, palavra) == palavra:
            print('Parabéns, você ganhou!')
            break
    
    else:
        erros += 1
        print('Letra errada')
        if erros>=6:
            print('Você perdeu')
            print('A palavra era: ', palavra)
            break
        print(exibicao(letras, palavra))
    print('Letras tentadas:', letras)
    print('Vidas restantes:', 6-erros)