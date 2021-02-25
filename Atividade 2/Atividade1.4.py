km = float(input("Quantos quilômetros o seu carro faz por litro: "))
litros = float(input("Quantos litros de gasolina há no momento: "))
x = float(input("Qual a distância que você deseja percorrer: "))

pera = x / km
calculo = (x / km) + litros

if pera < litros:
    print("Você precisa abastecer!!")
    print("Adicione mais {} litros".format(x / km - litros))


else:
    print("Boa viagem!!")