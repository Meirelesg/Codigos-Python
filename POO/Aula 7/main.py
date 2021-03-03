from Heranca2 import Aluno, Professor

a1 = Aluno("Matilda", 20, 987)
a1.mostreAluno()
print(f"A matrícula de {a1.nome} é {a1.matricula}")

p1 = Professor("Juliano",31,2500)
p1.mostraProfessor()
print(f"O salário de {p1.nome} é {p1.salario}")