#Crie um jogo de perguntas e respostas a partir de uma lista de questões com múltiplas alternativas 
# (ou verdadeiro/falso). O sistema deve apresentar uma pergunta de cada vez, 
# permitir que o usuário selecione uma resposta e, em seguida, informar se a resposta está correta, 
# atualizando uma pontuação.

import random

class questao:
    def __init__(self, pergunta, respostaC, errada1, errada2, errada3):
        self.pergunta = pergunta
        self.respostaC = respostaC
        self.errada1 = errada1
        self.errada2 = errada2
        self.errada3 = errada3

    def respostas(self):
        alternativas = [self.respostaC, self.errada1, self.errada2, self.errada3]
        a = random.choice(alternativas)
        alternativas.remove(a)
        print('A:', a)
        b = random.choice(alternativas)
        alternativas.remove(b)
        print('B:', b)
        c = random.choice(alternativas)
        alternativas.remove(c)
        print('C:', c)
        d = alternativas[0]
        print('D:', d)
        
        dic = {'a': a, 'b': b, 'c': c, 'd': d}
        return dic
    
    def getResposta(self):
        return self.respostaC
    
    def getPergunta(self):
        return self.pergunta

questao1 = questao('Quantos dentes tem um ser humano adulto?', '32', '36', '30', '34')
questao2 = questao('Quantos ossos tem um ser humano adulto?', '206', '200', '212', '220')
questao3 = questao('Quantos países existem no mundo?', '195', '180', '207', '175')
questao4 = questao('Quantos elementos tem na tabela perióica?', '118', '126', '115', '112')
questao5 = questao('Quantos joules equivale 1 waats?', '1', '7', '15', '30')

questoes = [questao1, questao2, questao3, questao4, questao5]
pontuacao = 0

print('Hora do quiz!')
print('A cada resposta certa você ganha 1 ponto no seu score')
print('A cada resposta errada você perde 1 ponto no seu score')
print('Vamos começar!\n')
for a in range (5):
   
    questaoEscolhida = random.choice(questoes)
    questoes.remove(questaoEscolhida)
    print(questaoEscolhida.getPergunta())
    gabarito = questaoEscolhida.respostas()
    
    entrada = input('Sua alternativa: ').lower()
    
    for i in gabarito:
        if entrada == i and gabarito[i]==questaoEscolhida.getResposta():
            print('Correto!')
            pontuacao += 1
        elif entrada == i and gabarito[i]!=questaoEscolhida.getResposta():
            print('Errado! A resposta correta é', questaoEscolhida.getResposta())
            pontuacao -= 1
        else: continue
    
print('Fim de jogo!')
print('Sua pontuação foi:', pontuacao)