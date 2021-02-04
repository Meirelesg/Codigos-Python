contador = 1
soma = 0
contadorN = 0

while contador <= 10:
    valor = int(input("Insira um valor, pelo amor de Deus: "))
    
    if valor < 0:
        contadorN = contador + 1
    else:
        soma = contador + valor
    contador = contador + 1
print("A soma dos valores positivos é: ", soma)
print("A quantidade de valores negativos é: ",contadorN)