vPermitida = float(input("Qual a velocidade permitida? R= "))
vMotorista = float(input("Qual a velocidade do motorista? R= "))

#Calcular 20% a mais 
vPermitida20 = (vPermitida * 0.2) + vPermitida

vPermitida50 =(vPermitida * 0.5) + vPermitida

if vMotorista <= vPermitida:
    print("Não precisa pagar multa xD")
elif vMotorista > vPermitida and vMotorista <= vPermitida20:
    print("Você cometeu uma infração média \nAssim irá pagar R$ 85.00 e receber 4 pontos na carteira")
elif vMotorista > vPermitida and vMotorista <= vPermitida50:
    print("Você cometeu uma infração grave \nAssim irá pagar R$ 127.00 e receber 5 pontos na carteira")
elif vMotorista > vPermitida50:
     print("Você cometeu uma infração trágica \nAssim irá pagar um rim e receber 7 pontos na carteira \nTer a carteira apreendida\ne ter o direito de dirigir suspenso")

