produtos = [
    "Pão 1kg", 9.00,
    "Leite", 9.59,
    "Café", 3.99,
    "Açúcar", 2.25,
    "Azeite", 16.99,
    "Arroz 5kg", 19
]

print("-"*40)
print(f"{'Lista de Compras':^40}")
print("-"*40)
for y,x in enumerate(produtos):
    if y % 2 ==0:
        print(f"{x:.<30}R$",end ="")
    else:
        print(f"{x:>8}")

print("-"*40)