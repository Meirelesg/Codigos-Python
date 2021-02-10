pessoas = {"Nome":"Bruno",
"Idade":21,
"Bairro":"Turu"
        }
print(pessoas)
print(f"Olá {pessoas['Nome']}, você tem {pessoas['Idade']} anos e mora no bairro {pessoas['Bairro']}")



print(pessoas.keys()) #Chaves são tudo antes dos ":" do dicionário
print(pessoas.values()) #Exibindo o conteúdo
print(pessoas.items()) #Exibindo itens chaves e valores
print("\n\n\n")

#Exibir as chaves, itens, valores

#for chave in pessoas.items():
#    print(chave)

#inserindo mais valores e chaves
pessoas.update({'sexo':'m'})

#pessoas.get('Idade')   ---- UM EXTRA NÃO MUITO CERTO KKK




#Preencher uma lista com dicionários
lista = []

for cont in range(0,2):
    pessoas["Nome"] = input("Informe o seu nome: ")
    pessoas["Idade"] = int(input("Informe sua idade: "))
    pessoas["Bairro"] = input("Informe seu Bairro: ")
    pessoas["sexo"] = input("Informe seu sekisu: ")

    lista.append(pessoas.copy())

print(lista)


print(lista[0]['Nome']) #Mostrando item dentro da lista