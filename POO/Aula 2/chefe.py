from funcionario import Funcionario


f1 = Funcionario("Judite","ADM",2000)
f1.relatorio()

f2 = Funcionario("Manel","Pedreiro",1000)

print(f"O salário de {f2.nome} é R$ {f2.sal}")