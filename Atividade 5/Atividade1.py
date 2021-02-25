mes = ("Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro")
temperaturaMes = []
valorTemp = 0
soma = 0
media = 0

for i in range(1,13):
    valorTemp = float(input(f"Insira a temperatura do {i}º mês: "))
    temperaturaMes.append(valorTemp)

for y in temperaturaMes:
    soma = soma + y

media = soma / 12

for indice,c in enumerate(temperaturaMes):
    if c > media:
        print(f"{mes[indice]:.<10}: {c}")
