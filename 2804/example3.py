from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.altura + self.largura)
    
class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        import math
        return math.pi * self.raio ** 2
    
    def calcular_perimetro(self):
        import math
        return math.pi * 2 * self.raio
    
ret = Retangulo(5, 10)
circ = Circulo(7)

print(f'Área do retângulo: {ret.calcular_area()}')
print(f'Perímetro do Círculo: {circ.calcular_perimetro()}')