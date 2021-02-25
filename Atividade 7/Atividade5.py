def idade(a):
    dicio = {}

    dias = a * 360
    meses = a * 12
    dicio['Meses'] = meses
    dicio['dias'] = dias

    print(dicio)


anos = int(input("Qual a sua idade, pelo amor de Deus: "))
idade(anos)

