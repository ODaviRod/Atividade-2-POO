# Considere os diagramas UML dos seguintes itens. Construa o código das
# respectivas classes, conforme definição dos métodos e crie 2 objetos usando o
# método construtor criado, e o preencha com dados fornecidos pelo usuário. Exiba os
# dados dos objetos.

class aluno:
    def __init__ (self, n, e, ra, i):
        self.nome = n
        self.endereco = e
        self.ra = ra
        self.idade = i
    def mostarDados(self):
        print("Nome: ", self.nome)
        print("Endereco: ", self.endereco)
        print("RA: ", self.ra)
        print("Idade: ", self.idade)

# Objeto 1
nome1 = str(input("Digite o nome do aluno 1: "))
endereco1 = str(input("Digite o endereco do aluno 1: "))
ra1 = str(input("Digite o RA do aluno 1: "))
idade1 = int(input("Digite a Idade do aluno 1: "))
aluno1 = aluno (nome1, endereco1, ra1, idade1)
aluno1.mostarDados()

# Objeto 2
nome2 = str(input("Digite o nome do aluno 2: "))
endereco2 = str(input("Digite o endereco do aluno 2: "))
ra2 = str(input("Digite o RA do aluno 2: "))
idade2 = int(input("Digite a Idade do aluno 2: "))
aluno2 = aluno (nome2, endereco2, ra2, idade2)
aluno2.mostarDados()
