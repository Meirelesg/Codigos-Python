def calculaImposto(sal, imposto = False):
    if imposto:
        desconto = float(input("Qual a porcentagem do imposto, pelo amor de Deus: "))
    else:
        desconto = 20
    desconto = desconto / 100
    return sal - (sal * desconto)


salario = int(input("Informe o seu salário: "))

print(f"Seu salário com desconto é R${calculaImposto(salario,True)}")
