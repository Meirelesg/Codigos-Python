'''
from os import system
system("cls")

print("="*15,"Exemplo 1","="*15)


valor = 1

while valor <= 10:
    print(valor)
    valor = valor + 1
'''


print("="*15,"Exemplo 2","="*15)
while True:
    num = int(input("Informe um valor qualquer: "))
    if num == 0:
        break #Finaliza o While
    