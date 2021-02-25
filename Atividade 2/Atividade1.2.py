peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

massa = peso / (altura**2)

if massa <= 16:
    print("Magreza grave")
elif massa > 16 and massa <= 17:
    print("Magreza moderada")
elif massa > 17 and massa <= 18.5:
    print("Magreza leve")
elif massa > 18.5 and massa <= 25:
    print("Saudável")
elif massa > 25 and massa <= 30:
    print("Sobrepeso")
elif massa > 30 and massa <= 35:
    print("Obesidade Grau I")
elif massa > 35 and massa <= 40:
    print("Obesidade Grau II")
elif massa > 40:
    print("Amigo tu tá gordinho hein...")

print("A massa é: ",massa)