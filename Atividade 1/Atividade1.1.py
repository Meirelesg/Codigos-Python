salario = float(input("Insira o seu salário que você recebe: "))
CH = int(input("Quantas horas você trabalha por dia: "))

horasTrabalhadas = salario / CH

print("Você receberá {:.2f} por horas trabalhadas".format(horasTrabalhadas))
