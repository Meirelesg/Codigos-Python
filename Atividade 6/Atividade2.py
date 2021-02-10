aluno = {}
turma = []

for x in range(0,3):
    aluno['nome'] = str(input("Insira o seu nome: ")).title()
    aluno['nota1'] = float(input("Isnira a 1° nota: "))
    aluno['nota2'] = float(input("Isnira a 2° nota: "))
    aluno['nota3'] = float(input("Isnira a 3° nota: "))

    aluno['media'] = (aluno['nota1'] + aluno['nota2'] + aluno['nota3']) / 3

    turma.append(aluno.copy())
    aluno.clear


print(turma,"\n\n\n")

for itens in turma:
    for chave, valor in itens.items():
        if chave == 'nome':
            print(f"Aluno(a) {valor},", end="")
        if chave == 'media':
            print(f" sua média é {valor:.2f}")
