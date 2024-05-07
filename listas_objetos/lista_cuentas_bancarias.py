from typing import List


class CuentaBancaria:
    def __init__(self, balance: float = 0.0):
        self.__balance: float = balance

    def depositar(self, cantidad: float) -> None:
        self.__balance += cantidad

    def retirar(self, cantidad: float) -> None:
        self.__balance -= cantidad

    def get_balance(self) -> float:
        return self.__balance

    def set_balance(self, balance: float):
        self.__balance = balance


def main():
    # Crear una lista para guardar objetos de CuentaBancaria
    lista_cuentas: List[CuentaBancaria] = []

    # Añadir 3 objetos CuentaBancaria a la lista
    lista_cuentas.append(CuentaBancaria(100.00))
    lista_cuentas.append(CuentaBancaria(500.00))
    lista_cuentas.append(CuentaBancaria(1500.00))

    # Mostrar cada elemento
    for index, cuenta in enumerate(lista_cuentas):
        print(f"Cuenta en el índice {index}\n"
              f"Balance: {cuenta.get_balance()}")

    # Quiero tener en la cuenta [0] $500.00. Hacer el depósito e imprimir su balance
    print("-" * 50)
    lista_cuentas[0].depositar(400)
    print("Balance de la cuenta[0]: ", end="")
    print(lista_cuentas[0].get_balance())

    # De la cuenta[1], pedir al usuario la cantidad a retirar.
    # Hacer el retiro e imprimir su balance------retirar $300, debe quedar $200

    print("-" * 50)
    cantidad_a_retirar: float = float(input("Dame cantidad a retirar: "))
    lista_cuentas[1].retirar(cantidad_a_retirar)
    print("Balance de la cuenta[1]: ", end="")
    print(lista_cuentas[1].get_balance())

    # El banco quiere saber el saldo total de todas las cuentas. Calcular y mostrar.
    print("-" * 50)

    saldo_total: float = 0.0
    for cuenta in lista_cuentas:
        saldo_total += cuenta.get_balance()

    print(f"El saldo total es de {saldo_total}")


if __name__ == "__main__":
    main()
