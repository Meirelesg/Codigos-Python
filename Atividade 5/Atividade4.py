frutas = []
valor = 0


for i in range(1,6):
    valor = str(input(f"Coloca as frutas aí boy: "))
    frutas.append(valor)

while True:
    print(f"{'Lista de Frutas':*^30}")
    
    for a, b in enumerate(frutas):
        print(f"{a:.<10} {b}")
    print("\n")
    print("0. Terminar")
    print("1. Inserir uma fruta")
    print("2. Excluir uma fruta")
    op = int(input("E ai? escolhe boy: "))

    if op == 0:
        break
    elif op == 1:
        frutas.append(input("Informe uma nova fruta: "))
    elif op == 2:
        ex = int(input("Qual a posição da fruta que tu quer remover, Cleitin?"))
        frutas.pop(ex)

print("\n\nObrigado, Cleitin '-'\n\n")