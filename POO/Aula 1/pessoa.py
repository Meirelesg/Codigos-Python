from datetime import date

class Pessoa:
    #Atributos
    nome = 'Juliano'
    idade = 21
    altura = 1.78

    #método
    def falar(self, texto):
        print(texto)
    '''def calculaAno(sefl,idade):
        anoAtual = date.today().year
        print(f"Você nasceu no ano de {anoAtual - idade}")'''

class Dog:
    nome = 'Pimpim'
    cor = 'marrom'
    olhos = 'castanhos'
    
    def correr(self):
        print("O dog está correndo")
    def latir(self):
        print("AU AU AU AU SAFADO!!!")
    def dormir(self):
        print("mimir")
