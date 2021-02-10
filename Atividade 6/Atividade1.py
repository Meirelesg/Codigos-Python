lanchonete = {
    'salgado': 4.90,
    'suco': 3.00,
    'refrigerante': 4.00,
    'Hamburgues': 7.20,
    'Doce': 2.00
}
print("-"*40)
print(f"{'Produtos            |            Preços'}")
print("-"*40)

for y,x in lanchonete.items():
    print(f"{y:.<33}R${x:>5}")
print("-"*40)
