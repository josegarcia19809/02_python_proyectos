class CuentaBancaria:
    # Constructor
    def __init__(self, balance_inicial) -> None:
        self.balance = balance_inicial

    # Método depositar servirá para agregar una cantidad a nuestra cuenta
    def depositar(self, cantidad):
        self.balance += cantidad

    # Método retirar servirá para quitar una cantidad a nuestra cuenta
    def retirar(self, cantidad):
        if self.balance >= cantidad:
            self.balance -= cantidad

    # Método get_balance servirá para obtener el balance actual de mi cuenta
    # obtener_balance  POO -> get_balance
    def get_balance(self):
        return self.balance

    # Método __str__ para retornar una cadena indicando el estado del objeto
    def __str__(self) -> str:
        return f"El balance es ${self.balance:,.2f}"
