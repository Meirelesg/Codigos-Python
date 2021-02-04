contador = 0

while True:
    valor = int(input("Insira um valor inteiro: "))

    if valor == 0:
        break
    if contador == 0:
        maior = valor
        menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
    contador = contador + 1


print("O maior valor é: ",maior)
print("O menor valor é: ", menor)

    
    