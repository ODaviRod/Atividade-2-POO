class Produto:
    def __init__ (self, m, f, cb, p):
        self.marca = m
        self.facricante = f
        self.cod_barras = cb
        self.preco = p 
    def imprimir(self):
        print("Marca: ", self.marca)
        print("fabricante: ", self.facricante)
        print("Código de Barras: ", self.cod_barras)
        print("Preço: ", self.preco)

# Objeto 1

marca1 = str(input("Digite a marca do produto 1: "))
fabricante1 = str(input("Digite o fabricante do produto 1: "))
cod1 = str(input("Digite o Código de Barras do produto 1: "))
preco1 = float(input("Digite o preço do produto 1: "))
produto1 = Produto (marca1, fabricante1, cod1, preco1)
produto1.imprimir()

# Objeto 2

marca2 = str(input("Digite a marca do produto 2: "))
fabricante2 = str(input("Digite o fabricante do produto 2: "))
cod2 = str(input("Digite o Código de Barras do produto 2: "))
preco2 = float(input("Digite o preço do produto 2: "))
produto2 = Produto (marca2, fabricante2, cod2, preco2)
produto2.imprimir()