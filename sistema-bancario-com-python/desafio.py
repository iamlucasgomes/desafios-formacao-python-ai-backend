from datetime import datetime
from uuid import uuid4


class SistemaBancario:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__saldo = 0
        self.__historico = []
        self.__saques = 0
        self.__ultima_data_saque = None

    def __deposito(self, valor: int):
        if valor <= 0:
            return print("Valor deve ser maior que zero")
        else:
            self.__saldo += valor
            self.__historico.append(
                {
                    "id": uuid4(),
                    "data": datetime.now().date().isoformat(),
                    "valor": valor,
                    "operacao": "Depósito",
                }
            )

            return print(f"Depósito realizado com sucesso! Saldo atual: {self.__saldo}")

    def __saque(self, valor: int):

        hoje = datetime.now().date()

        if self.__saldo <= 0 or self.__saldo < valor:
            return print("Saldo insuficiente")

        if valor > 500:
            return print("Valor máximo para saque é de R$500")

        if self.__saques >= 3:
            return print("Limite de saques excedido")

        else:
            if self.__ultima_data_saque != hoje:
                self.__saques = 0
                self.__ultima_data_saque = hoje

            self.__saldo -= valor
            self.__saques += 1
            self.__historico.append(
                {
                    "id": uuid4(),
                    "data": datetime.now().date().isoformat(),
                    "valor": valor,
                    "operacao": "Saque",
                }
            )
            return print(f"Saque realizado com sucesso! Saldo atual: {self.__saldo}")

    def __extrato(self):
        print("---- Extrato ----")
        print(f"Cliente: {self.__nome}")
        if len(self.__historico) == 0:
            print("Não foram realizadas movimentações")

        for transacao in self.__historico:
            operacao = transacao["operacao"]
            valor = transacao["valor"]
            print(f"{operacao}: R${valor:.2f}")

        print(f"Saldo atual: R${self.__saldo:.2f}")
        print("-----------------")

    def operacoes(self):
        menu = """

            [d] Depositar
            [s] Sacar
            [e] Extrato
            [q] Sair

            => """
        operacao_selecionada = input(menu)
        match operacao_selecionada:
            case "d":
                valor = int(input("Digite o valor do depósito: "))
                self.__deposito(valor)
                self.operacoes()
            case "s":
                valor = int(input("Digite o valor do saque: "))
                self.__saque(valor)
                self.operacoes()
            case "e":
                self.__extrato()
                self.operacoes()
            case "q":
                return print("até mais!")


# Testando o código

cliente1 = SistemaBancario("João")
cliente1.operacoes()
