somando = 0

for a in range(0,11):
    idade = int(input("Informe a sua idade: "))
    somando = somando + idade
    media = somando / 10

if media <= 25:
    print("A Turma é jovem")
elif media > 25 and media <= 60:
    print("A tuma é Adulta") 
elif media > 60:
    print("A turma é Idosa")
    
    