import math

class Forma:
    def calcular_area(self):
        return 0  # Forma genérica (base)

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

# Usando polimorfismo:
formas = [Retangulo(5, 3), Circulo(2)]

for forma in formas:
    print("Área:", forma.calcular_area())
