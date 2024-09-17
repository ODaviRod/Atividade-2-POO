# Considere os diagramas UML dos seguintes itens. Construa o código das respectivas
# classes, conforme definição dos métodos e crie 2 objetos usando o método construtor
# criado, e o preencha com dados fornecidos pelo usuário. Calcule a área dos objetos e
# exiba os dados dos objetos correspondentes.

class Circulo:
    def __init__ (self, r: float,):
        self.raio = r
        self.area = None
        self.pi = 3.1415
    
    def calcularArea (self):
        self.area = (self.pi + (self.raio*self.raio))
    
    def mostrarDados (self):
        print("Raio: ", self.raio)
        print("Área: ", self.area)
    
raio = float(input("Digite o raio do circulo: "))
circulo1 = Circulo(raio)
circulo1.calcularArea()
circulo1.mostrarDados()
