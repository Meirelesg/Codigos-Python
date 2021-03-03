from associacao import Celular, Pessoa

smartphone = Celular("Xiaomi",1500)

p1 = Pessoa("Random",45,"Rua del chavo")

print(f"{p1.nome} mora no endereço {p1.endereco} e tem {p1.idade} anos")

p1.celular = smartphone

print(f"{p1.nome} possui um celular da marma {p1.celular.marca} e custou {p1.celular.valor}")