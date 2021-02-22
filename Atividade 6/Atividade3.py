from os import system
from time import sleep

contato = {}
listaContato = []

while True:
    system("cls")
    print("="*40)
    print(f"{'Agenda':^40}")
    print("="*40)
    
    for itens in listaContato:
        for chave, valor in itens.items():
            print(f"{chave}:{valor}")
    
    print("1. Insrir um contato!")
    print("2. Excluor um contato")
    print("3. Sair")
    op = int(input("E ai? o que me diz? "))

    if op == 3:
        break
    elif op == 1:
        nome = str(input("Insira informe o nome do contato: ")).title()
        fone = int(input("Insira o seu tefelone: "))
        
        
        contato[nome] = fone #Trocando a chave('nome') para o nome da pessoas//// Trocando o valor('nome') para o número
        listaContato.append(contato.copy())
        
        contato.clear
    elif op == 2:
        escolha = str(input("Informe o nome da pessoa que deseja exluir: ")).title()
        for itens in listaContato:
            if escolha in itens.keys():
                itens.pop(escolha)
            else:
                print("Todo burro ¬¬'")
                sleep(1)


print("="*40)


