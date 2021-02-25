lista = []

for cont in range(20):
    lista.append(cont)
print(lista)

numeros = [cont for cont in range(20)]      #Mesma coisa que o de cima

print(numeros)

#Utilizar Lambda
soma = lambda x,y: (x + y) + 5
print(soma(4,5))


#usando M.A.P --> ( função    ,     lista  )

dobro = list(map(lambda x: x*2, lista))

print(dobro)