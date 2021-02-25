lista = []



def listaNomes():
    while True:
        lista.append(str(input("Infome um nome aí, cleitin: ")).title())
        opc = str(input("Deseja continuar? s/n: ")).lower()

        if opc == 'n':
            break
        
def exluiNomes():
    for indice,nomes in enumerate(lista):
        print(f"{indice}: {nomes}")
        posi = int(input("Insira a posição da pessoa que você quer excluir: "))
        print("\nfoi deletado ;-;\n")
        lista.pop(posi)


while True:
    print("1 - Inserir nomes. ")
    print("2 - Exluir nomes. ")
    print("3 - Sair.")

    op = int(input("Escolhe ai amigão: "))
    if op == 1:
        listaNomes()
    elif op == 2:
        exluiNomes()
    elif op == 3:
        break
