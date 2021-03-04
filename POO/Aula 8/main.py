from polimorfismo import Pessoa, Aluno, Fessor


p1 = Pessoa("Munique")

p1.cpf = "11111111111"
p1.exibirDados()
print("\n\n")

a1 = Aluno("Judindin",123,"Ciências Biológicas")
a1.exibirDados()
print("\n\n")

f1 = Fessor("Annie", 2300, 5)
f1.exibirDados()