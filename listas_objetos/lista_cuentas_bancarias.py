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


if __name__ == "__main__":
    # Crear una lista para guardar objetos CuentaBancaria
    lista_cuentas: List[CuentaBancaria] = []

    # Añadir 3 objetos CuentaBancaria a la lista
    lista_cuentas.append(CuentaBancaria(100.0))
    lista_cuentas.append(CuentaBancaria(500.0))
    lista_cuentas.append(CuentaBancaria(1500.0))

    # Mostrar cada elemento
    for index, cuenta in enumerate(lista_cuentas):
        print(f"Cuenta en el índice {index}\nBalance: {cuenta.get_balance()}")
