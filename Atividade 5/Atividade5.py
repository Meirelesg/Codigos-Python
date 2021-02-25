from random import randint

aleatorio = []

for c in range(1,21):
    aleatorio.append(randint(1,900))

for y in range(3,0,-1):
    print(f"Você só tem mais {y} tentativas")
    op = int(input("Informe um valor: "))
    
    if op in aleatorio:
        print(f"{'Acertoooouuuuuu':*^40}")
        print("Que cara bom   ¬¬'")

        break
    else:
        print("Errou rude amigão ^^")

print(aleatorio,"\n\n\n")