# Considere os diagramas UML dos seguintes itens. Construa o código das respectivas
# classes, conforme definição dos métodos e crie 2 objetos usando o método construtor
# criado, e o preencha com dados fornecidos pelo usuário. Calcule as áreas dos objetos
# e exiba os dados dos objetos correspondentes.

class Quadrado:
    def __init__(self, la: float):
        self.lado = la
        self.area = "Lado ainda não especificado..."

    def calcularArea(self):
        self.area = self.lado*self.lado

    def mostrarDados(self):
        print("Lado: ", self.lado)
        print("Área: ", self.area)

la = float(input("Digite o lado do quadrado: "))
quadrado1 = Quadrado(la)
quadrado1.calcularArea()
quadrado1.mostrarDados()



