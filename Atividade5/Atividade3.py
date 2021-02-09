num = []
valor = 0


for i in range(1,11):
    valor = int(input(f"Insira o {i}º valor: "))
    num.append(valor)

for hin,c in enumerate(num):
    print(f"a posição -> {hin} o número é -> {c}")
posi1 = int(input("Escolha uma posição: "))
posi2 = int(input("Escolha outra posição: "))

print(f"{num[posi1]} x {num[posi2]} = {num[posi2] * num[posi2]}")
print(f"{num[posi1]} : {num[posi2]} = {num[posi2] / num[posi2]}")
print(f"{num[posi1]} + {num[posi2]} = {num[posi2] + num[posi2]}")
print(f"{num[posi1]} - {num[posi2]} = {num[posi2] - num[posi2]}")
print(f"{num[posi1]} elevado {num[posi2]} = {num[posi2] ** num[posi2]}")