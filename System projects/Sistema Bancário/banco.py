class Conta:
    
    def __init__(self,numero,titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0.0
        self.historico = []

    def depositar(self,valor):
        if valor <= 0:
            print("Valor inválido.")
            return
        
        self.saldo += valor
        self.historico.append(f"Depósito: R${valor:.2f}")
        print("Depósito realizado com sucesso!")

    def sacar(self,valor):
        if valor <= 0:
            print("Valor inválido.")
            return
        
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return
    
        self.saldo -= valor
        self.historico.append(f"Saque: R${valor:.2f}")
        print("Saque realizado com sucesso!")

    def transferir(self,destino,valor):
        if valor <= 0:
            print("Valor inválido.")
            return
        
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return
        
        self.saldo -= valor
        destino.saldo += valor

        self.historico.append(
            f"Transferência enviada: R${valor:.2f} para {destino.numero}"
        )

        destino.historico.append(
            f"Transferência recebida: R${valor:.2f} de {self.numero}"
        )

        print("Transferência realizada!")

    def extrato(self):
        print("\n=== Extrato ===")

        if not self.historico:
            print("Nenhuma movimentação.")

        for item in self.historico:
            print(item)

        print(f"\nSaldo atual: R${self.saldo:.2f}")

class Banco:
    
    def __init__(self):
        self.contas = {}

    def criar_conta(self):
        numero = input("Número da conta: ")

        if numero in self.contas:
            print("Conta já existe.")
            return
        
        titular = input("Nome do titular: ")

        self.contas[numero] = Conta(numero,titular)
        
        print("Conta criada com sucesso!")

    def buscar_conta(self,numero):
        return self.contas.get(numero)
    
    def listar_contas(self):
        print("\n=== Contas Cadastradas ===")

        if not self.contas:
            print("Nenhuma conta cadastrada.")
            return
        
        for conta in self.contas.values():
            print(
                f"Conta: {conta.numero} |"
                f"Títular: {conta.titular} |"
                f"Saldo: R${conta.saldo:.2f}"
            )

def selecionar_conta(banco):
        numero = input("Número da conta: ")

        conta = banco.buscar_conta(numero)

        if not conta:
            print("Conta não encontrada.")
            return None
        
        return conta
    
def menu():
    banco = Banco()

    while True:
        print("\n===== SISTEMA BANCÁRIO =====")
        print("1 - Criar conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Transferir")
        print("5 - Consultar saldo")
        print("6 - Extrato")
        print("7 - Listar contas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            banco.criar_conta()

        elif opcao == "2":
            conta = selecionar_conta(banco)

            if conta:
                valor = float(input("Valor do depósito: "))
                conta.depositar(valor)

        elif opcao == "3":
            conta = selecionar_conta(banco)

            if conta:
                valor = float(input("Valor do saque: "))
                conta.sacar(valor)

        elif opcao == "4":
            origem = selecionar_conta(banco)

            if origem:
                
                destino_numero = input(
                    "Conta de destino: "
                )
                destino = banco.buscar_conta(
                    destino_numero
                )

                if not destino:
                    print("Conta destino não encontrada.")
                    continue

                valor = float(
                    input("Valor da transferência: ")
                )

                origem.transferir(destino,valor)

        elif opcao == "5":
            conta = selecionar_conta(banco)

            if conta:
                print(
                    f"Saldo atual: "
                    f"R${conta.saldo:.2f}"
                )

        elif opcao == "6":
            conta = selecionar_conta(banco)

            if conta:
                conta.extrato()

        elif opcao == "7":
            banco.listar_contas()

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")

menu()