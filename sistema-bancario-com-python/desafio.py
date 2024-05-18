from datetime import datetime
from uuid import uuid4


class SistemaBancario:
    def __init__(self, nome: str, saldo: int):
        self.nome = nome
        self.saldo = saldo
        self.historico = []
        self.saques = 0
        self.ultima_data_saque = None

    def deposito(self, valor: int):
        if valor <= 0:
            raise ValueError("Valor deve ser maior que zero")
        else:
            self.saldo += valor
            self.historico.append(
                {
                    "id": uuid4(),
                    "data": datetime.now().date().isoformat(),
                    "valor": valor,
                    "operacao": "Depósito",
                }
            )

            return f"Depósito realizado com sucesso! Saldo atual: {self.saldo}"

    def saque(self, valor: int):

        hoje = datetime.now().date()

        if self.saldo == 0:
            return print("Saldo insuficiente")

        if valor > 500:
            return print("Valor máximo para saque é de R$500")

        if self.saques >= 3:
            return print("Limite de saques excedido")

        else:
            if self.ultima_data_saque != hoje:
                self.saques = 0
                self.ultima_data_saque = hoje

            self.saldo -= valor
            self.saques += 1
            self.historico.append(
                {
                    "id": uuid4(),
                    "data": datetime.now().date().isoformat(),
                    "valor": valor,
                    "operacao": "Saque",
                }
            )
            return f"Saque realizado com sucesso! Saldo atual: {self.saldo}"

    def extrato(self):
        print("---- Extrato ----")
        if len(self.historico) == 0:
            print("Não foram realizadas movimentações")

        for transacao in self.historico:
            operacao = transacao["operacao"]
            valor = transacao["valor"]
            print(f"{operacao}: R${valor:.2f}")

        print(f"Saldo atual: R${self.saldo:.2f}")
        print("-----------------")


# Testando o código

cliente1 = SistemaBancario("João", 1000)
print(cliente1.deposito(500))
print(cliente1.saque(600))
print(cliente1.saque(200))
print(cliente1.saque(200))
print(cliente1.saque(200))
cliente1.extrato()