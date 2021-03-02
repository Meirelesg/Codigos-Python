class Funcionario:
    #Criando o método construtor
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.sal = salario


    '''
    nome = 'Juliano'
    cargo = 'Padeiro'
    salario = 1100
    '''


    def relatorio(self):
        print(f"Nome: {self.nome},Cargo: {self.cargo}, Salário: {self.sal}")


