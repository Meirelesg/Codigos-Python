def gente(a,b):
    contar = 0
    for i in frase:
        if letra == i:
            contar = contar + 1

    print(f"A letra '{letra}' aparece {contar}x, Uau e.e ")

frase = str(input("Insira uma frase bem Kawaii: ")).lower()
letra = str(input("Insira uma letra: "))
gente(frase,letra)
