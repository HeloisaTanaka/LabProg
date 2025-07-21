# is verifica se existe
# a variável c não é criada até que seja atribuída um valor a ela, aí ele é criado na memória
# c=None é diferente de def somar(self, a, b, c=None), 
# no primeiro o c exite e seu valor é nulo (c==None)
# no segundo o c não existe, ele é Nulo por si só (c is None)

class Calculadora:
    def somar(self, a, b, c=None):
        if c is None:
            return a + b
        else: 
            return a + b+ c
        
calc = Calculadora()
print(calc.somar(2, 3))
print(calc.somar(2, 3, 4))
