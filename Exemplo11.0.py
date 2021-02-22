from datetime import date
anoAtual = date.today().year
def divisoria():
    print("-"*50)
nome = str(input("Insira seu nome, viajante: "))
divisoria()

idade = int(input("Informe sua idade, viajante:  "))
divisoria()

print(f"{nome} sua idade é {idade}.")
print("E você nasceu no ano de: ", anoAtual - idade)