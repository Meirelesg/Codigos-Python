class Cliente:
    def __init__(self, nome, telefone, cpf, endereco):
        self.nome = nome
        self.telefone = telefone
        self.cpf = cpf
        self.endereco = endereco

class Conta:
    def __init__(self, numero, cliente, saldo,limite = 1000):
        self.numero = numero
        self.cliente = cliente
        self.limite = limite
        self.saldo = saldo