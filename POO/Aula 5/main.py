from agregacao import Cliente, Conta

c1 = Cliente("Chiquinha","98 4002 8922","123.456.789 - 55", "Rua dos Reis 35, bairro das Valas")

conta1 = Conta(1234,c1,1100,2000)

print(f"O cliente {conta1.cliente.nome} possui o saldo de R${conta1.saldo} e mora no endereço {conta1.cliente.endereco} e possui o telefone {conta1.cliente.telefone} e um limite de compras de {conta1.limite}")