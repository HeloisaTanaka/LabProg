#Crie uma superclasse funcionário com os atributos nome e salário base, e método calcular salário
#Crie uma subclasse gerente com atributo bônus
#Crie uma subclasse vendedor com atributos comissão e vendas
#Crie uma subclasse chamada desenvolvedor com os atributos nível e experiência

#implemente o método calcular salário , considerando os atributos de cada classe

#bonus = 500
#comissao = 200
#vendas = 300
#nivel = 3
#expe = 400

class func:
    def __init__ (self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_sal(self):
        print(self.salario)

class gerente(func):
    def __init__ (self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def calcular_sal(self):
        print('Salário do gerente:', self.salario + self.bonus)

class vendedor(func):
    def __init__ (self, nome, salario, comissao, vendas):
        super().__init__(nome, salario)
        self.comissao = comissao
        self.vendas = vendas

    def calcular_sal(self):
        print('Salário do vendedor:', self.salario + self.vendas + self.comissao)

class desenvolvedor(func):
    def __init__ (self, nome, salario, nivel, expe):
        super().__init__(nome, salario)
        self.nivel = nivel
        self.expe = expe

    def calcular_sal(self):
        print('Salário do desenvolvedor:', self.salario * self.nivel + self.expe)

pessoa1 = gerente('Ricardo', 1500, 500)
pessoa2 = vendedor('Giovanna', 1100, 200, 40)
pessoa3 = desenvolvedor('Miguel', 2000, 4, 300)
pessoa1.calcular_sal()
pessoa2.calcular_sal()
pessoa3.calcular_sal()