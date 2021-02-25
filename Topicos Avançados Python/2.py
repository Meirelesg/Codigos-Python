#vamos trabalhar com função filter

valores = list(range(20,61))
print(valores)


#                  (1º vem a função  , a lista)
pares = list(filter(lambda x: x%2==0,valores))
print("Os números pares são: \n",pares)