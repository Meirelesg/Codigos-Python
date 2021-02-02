nota1 = float(input("Digite a 1º nota: "))
nota2 = float(input("Digite a 2º nota: "))
nota3 = float(input("Digite a 3º nota: "))

media = (nota1 + nota2 + nota3)/3

#if media > 7:
#   print("Você foi aprovado!!")
#else:
#   print("Você é uma desgraça... e não foi aprovado!")

if media > 7:
    print("Você foi aprovado")
elif media == 7:
    print("Quase hein, tafarél")
else:
    print("Que desgraça, tu não foi aprovado boy")

