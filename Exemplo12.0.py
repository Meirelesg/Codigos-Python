def calculoImposto(sal,imposto = 20):
    imposto = imposto / 100 #calcular a porcentagem do valor k
    novoSalario = sal - (salario * imposto)
    return novoSalario

salario = float(input("insira seu salário, viajante: "))
#porc = float(input("Informe a porcentagem de desconto: "))


print(f"O seu salário agora é RS{calculoImposto(salario)}")
