def somatorio(a):
    somando = 0
    for i in range(valor+1):
        somando = somando + i
        if i == valor:
            print(f"{i}={somando}")
        else:
            print(f"{i}",end="+")

valor = int(input("Insira um valor: "))
somatorio(valor)