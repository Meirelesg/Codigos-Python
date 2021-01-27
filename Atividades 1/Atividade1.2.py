produto1 = float(input("Insira o valor do 1º produto: "))
produto2 = float(input("Insira o valor do 2º produto: "))
produto3 = float(input("Insira o valor do 3º produto: "))

soma = produto1 + produto2 + produto3
desconto = 0.2
total = soma - (soma * desconto)

print("O total das compras foi de ", soma)
print("O desconto vai ser de ", soma * desconto,)
print("O cliente deve pagar ",total)