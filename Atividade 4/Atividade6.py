from datetime import date

atual = date.today().year

while True:
    nascimento = int(input("Informe o ano do seu nascimento: "))
    idade = atual - nascimento
    if idade >= 18:
         print("Parabéns desgraça \(^-^)/")
    else:
        print("Sai daqui miséra!!!!")