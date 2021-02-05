pessoas = ["Diene","Vivian","Charles","Mercedes"]


print(pessoas)

pessoas[3] = "Cecília"         #Mudando elementos
pessoas.append("Karin")        #Adicionando um novo elemento no final da lista
pessoas.insert(1,"Elena")      #Adicionando um novo elemento no local desejado da lista


'''
for valor in pessoas:
    print(valor)


pessoas.pop()                  #Removendo o ultimo elemento da lista
pessoas.pop(0)                 #Removendo o elemento desejado da lista
pessoas.remove("Elena")        


print(pessoas)

'''

'''

pessoas.clear                  #Limpa a lista 
del(pessoas)                   #Apagar a lista
print(pessoas,"\n\n")

'''
'''
pessoasbkp = pessoas           #Copiando uma lista para outra {COM LIGAÇÃO ENTRE ELAS}

pessoasbkp.append("Charllote") 

pessoasbkp = pessoas{:}        #Copiando uma lista para outra {100 LIGAÇÃO ENTRE ELAS}

print(pessoas)  

print(pessoasbkp)
'''