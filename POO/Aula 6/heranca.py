#Herança Simples
class Humano:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__ #"__class__" pega o nome da classe


    def mostraClasse(self):
        print(f"{self.nomeClasse} = Seu nome é: {self.nome}")

class Aluno(Humano):
    def mostreAluno(self):
        print(f"{self.nomeClasse} = Sou um estudante e o meu nome é: {self.nome}")


class Professor(Humano):
    def mostraProfessor(self):
        print(f"{self.nomeClasse} = Sou professor e meu nome é: {self.nome}")
    
    

