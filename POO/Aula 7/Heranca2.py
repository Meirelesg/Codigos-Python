#Herança Simples
class Humano:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__ #"__class__" pega o nome da classe


    def mostraClasse(self):
        print(f"{self.nomeClasse} = Seu nome é: {self.nome}")

class Aluno(Humano):
    def __init__(self,nome, idade, matricula):
        Humano.__init__(self, nome, idade)
        self.matricula = matricula
        
    def mostreAluno(self):
        print(f"{self.nomeClasse} = Sou um estudante e o meu nome é: {self.nome}")


class Professor(Humano):
    def __init__(self,nome, idade, salario):
        Humano.__init__(self, nome, idade)
        self.salario = salario
    def mostraProfessor(self):
        print(f"{self.nomeClasse} = Sou professor e meu nome é: {self.nome}")
        
    

