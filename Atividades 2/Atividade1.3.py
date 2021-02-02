produto1 = float(input("Insira o valor de 1º produto: ")) 
produto2 = float(input("Insira o valor de 2º produto: ")) 
produto3 = float(input("Insira o valor de 3º produto: "))

if produto1 < produto2 < produto3:
    print("Você deve comprar o 1º produto: ", produto1)
elif produto2 < produto3 < produto1:
    print("Você deve comprar o 2º produto: ",produto2)
elif produto3 < produto2 < produto1:
    print("Você deve comprar o 3º produto: ",produto3)