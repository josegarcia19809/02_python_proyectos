class CuentaBancaria:
    # Constructor
    def __init__(self, balance_inicial):
        self.balance = balance_inicial

    def depositar(self, cantidad):
        """Servirá para agregar una cantidad a nuestra cuenta"""
        self.balance += cantidad

    def retirar(self, cantidad):
        """Servirá para quitar una cantidad a nuestra cuenta"""
        if self.balance >= cantidad:
            self.balance -= cantidad

    def get_balance(self) -> float:
        """Servirá para obtener el balance actual de mi cuenta"""
        return self.balance

    def __str__(self) -> str:
        return f"El balance es ${self.get_balance():,.2f}"
