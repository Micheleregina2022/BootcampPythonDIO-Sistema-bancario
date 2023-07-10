class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)

    def sacar(self, valor):
        if 0 < valor <= 500 and len(self.saques) < 3 and self.saldo >= valor:
            self.saldo -= valor
            self.saques.append(valor)
        else:
            print("Não foi possível realizar o saque.")

    def extrato(self):
        print("Extrato:")
        if len(self.depositos) == 0 and len(self.saques) == 0:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


def main():
    banco = Banco()

    banco.depositar(3000.50)
    banco.depositar(700.75)
    banco.sacar(500)
    banco.depositar(780.25)

    banco.extrato()


if __name__ == "__main__":
    main()
