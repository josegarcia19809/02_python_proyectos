from cuenta_bancaria import CuentaBancaria

print("-"*100)
def main():
    # Pedir el balance inicial
    balance_inicial = float(input("Ingresa tu balance inicial: "))

    # Crear un objeto de CuentaBancaria
    ahorros = CuentaBancaria(balance_inicial)

    # Depositar a la cuenta del usuario
    pago = float(input("¿Cuánto te pagaron esta semana? "))
    print("Ese pago se depositará en tu cuenta.")
    ahorros.depositar(pago)

    # Mostrar el balance
    print(f"El balance de tu cuenta es ${ahorros.get_balance():,.2f}.")

    # Pedir una cantidad a retirar
    efectivo = float(input("¿Cuánto te gustaría retirar? "))
    print("Se retirará esa cantidad de tu cuenta")
    ahorros.retirar(efectivo)

    # Mostramos nuevamente el balance
    print(ahorros)


if __name__ == "__main__":
    main()

"""
Balance inicial: 5000
pago: 3000
retirar: 4000
Balance final debe ser $4000.00
"""
