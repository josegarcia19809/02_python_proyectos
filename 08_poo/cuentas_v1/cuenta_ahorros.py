class CuentaAhorro:
    # constructor
    def __init__(self, balance_inicial):
        self.balance = balance_inicial

    def __str__(self) -> str:
        return f"Balance: {self.balance}"

    def sacar_dinero(self, cantidad):
        if cantidad <= self.balance:
            print(f"Sacando {cantidad}")
            self.balance -= cantidad
        else:
            print(f"No tienes fondos para sacar {cantidad}")
