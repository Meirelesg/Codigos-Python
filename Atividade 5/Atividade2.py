valores = list()
pares = []

for cont in range(0,5):
    valores.append(int(input(f"Isnira o {cont+1}º valor: ")))

    if valores[cont] % 2 == 0:
        pares.append(valores[cont])


for cont in range(0,len(pares)):
    if pares[cont] in valores:
        valores.remove(pares[cont])

del(pares)
print(f"Lista sem os valores pares: {valores}")

