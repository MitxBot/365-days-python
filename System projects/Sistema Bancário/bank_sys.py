class Conta:
    
    def __init__(self,titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor

        else:
            print("Saldo insuficiente!")

    def mostrar_saldo(self):
        print(f"Saldo: R${self.saldo:.2f}")

conta = Conta("Usuário")

conta.depositar(1000)
conta.sacar(250)

conta.mostrar_saldo()