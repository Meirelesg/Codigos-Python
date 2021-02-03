import time
import os

pessoas = int(input("Quantas pessoas merecem um >>>boas-vindas<<: "))
H = 0
F = 0

for a in range(0,pessoas):
    nome = str(input("Qual o seu nome: "))
    sexo = str(input("Qual o seu sexo: "))
    
    if sexo == "Masculino":
        H = H + 1
        print("Bem vindo Sr. ",nome)
    else:
        F = F + 1
        print("Bem vinda Sra.",nome)
    
    time.sleep(1)  #Esperando 1 segundo xD
    ost.system("cls") #Limpa tela

print("A Quantidade de Homens é de: ", H)
print("A Quantidade de Mulheres é de: ", F)