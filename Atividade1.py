class Paciente:
    def __init__ (self, n, rg, end, tel, dataN, prof):
        self.nome = n
        self.rg = rg
        self.endereco = end
        self.telefone = tel
        self.dataNascimento = dataN
        self.professor = prof
    def imprimir(self):
        print("Nome: ", self.nome)
        print("RG: ", self.rg)
        print("Endereço: ", self.endereco)
        print("Telefone: ", self.telefone)
        print("Data de Nascimento: ", self.dataNascimento)
        print("Professor: ", self.professor)

# Objeto 1

nome1 = str(input("Digite o nome do paciente 1: "))
rg1 = float(input("Digite o RG do paciente 1: "))
end1 = str(input("Digite o Endereço do paciente 1: "))
tel1 = str(input("Digite o telefone do paciente 1: "))
dataN1 = str(input("Digite a data de nascimento do paciente 1: "))
prof1 = str(input("Digite o nome do Professor do Paciente 1: "))
paciente1 = Paciente (nome1, rg1, end1, tel1, dataN1, prof1)
paciente1.imprimir()

# Objeto 2

nome2 = str(input("Digite o nome do paciente 2: "))
rg2 = float(input("Digite o RG do paciente 2: "))
end2 = str(input("Digite o Endereço do paciente 2: "))
tel2 = str(input("Digite o telefone do paciente 2: "))
dataN2 = str(input("Digite a data de nascimento do paciente 2: "))
prof2 = str(input("Digite o nome do Professor do Paciente 2: "))
paciente2 = Paciente (nome2, rg2, end2, tel2, dataN2, prof2)
paciente2.imprimir()