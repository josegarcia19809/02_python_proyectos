from cuenta_bancaria import CuentaBancaria


def main():
    # Pedir el balance inicial
    balance_inicial = float(input("Ingresa tu salario inicial: "))

    # Crear un objeto de CuentaBancaria
    ahorros = CuentaBancaria(balance_inicial)

    # Depositar a la cuenta del usuario
    pago = float(input("¿Cuánto te pagaron esta semana? "))
    print("Ese pago se depositará a tu cuenta")
    ahorros.depositar(pago)

    # Mostrar el balance
    print(ahorros)

    # Pedir una cantidad a retirar
    retiro = float(input("¿Cuánto vas a retirar? "))
    print("Esa cantidad se retirará de tu cuenta")
    ahorros.retirar(retiro)
    # Mostrar nuevamente el balance
    print(ahorros)


if __name__ == "__main__":
    main()
