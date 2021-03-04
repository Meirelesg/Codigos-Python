class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.__cpf = ""

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, valor):
        if len(valor) != 11:
            print("O CPF precisa ter exatamente 11 dígitos!!")
        elif valor.isnumeric():
            self.__cpf = valor
        else:
            print("Insira apenas números")

    def exibirDados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.__cpf}")

class Aluno(Pessoa):
    def __init__(self, nome, matricula, curso = ""):
        super().__init__(nome)    #"Super" Tá ali pra subistituir o "Pessoa"
        self.matricula = matricula
        self.curso = curso

    def exibirDados(self):
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Curso: {self.curso}")
class Fessor(Pessoa):
    def __init__(self, nome, salario, cargaHoraria):
        super().__init__(nome)
        self.salario = salario
        self.cargaHoraria = cargaHoraria
    
    def exibirDados(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.salario}")
        print(f"Carga Horária (hrs/dia): {self.cargaHoraria}")