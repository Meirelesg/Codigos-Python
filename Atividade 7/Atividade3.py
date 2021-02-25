from random import randint

def palpite(a):
    soma = 1
    while a != valor:
        
        if a > valor:
            print("Seu palpite está acima do valor\n")
        else:
            print("Seu palpite está abaixo do valor\n")
        a = int(input("tente novamente: "))
        
        soma = soma + 1
    print(f"Você precisou de {soma} tentativas para acertar")

    



valor = randint(1,100)

print(valor)

voto = int(input("Qual número você acha que foi sorteado entre 1 e 100, Cleitin: "))

palpite(voto)

