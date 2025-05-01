# Definição da classe Cliente
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"Cliente: {self.nome}, Telefone: {self.telefone}"

# Definição da classe Conta
class Conta:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def __str__(self):
        return f"Conta {self.numero} - Titular: {self.titular.nome}, Saldo: R$ {self.saldo:.2f}"

# Testando o projeto
print("Testando o projeto")

# Criando cliente e conta
c1 = Cliente("João", "114444-2222")
conta1 = Conta(c1, "1234-5", 1000.00)

print(c1)
print(conta1)