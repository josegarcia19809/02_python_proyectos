from cuenta_ahorro import CuentaAhorro, CD

# Este programa crea una instancia de la clase CuentaAhorro
# y una instancia de la cuenta CD.
print("-" * 100)


def main():
    # Obtener el número de cuenta, la tasa de interés,
    # y el saldo de la cuenta de ahorros.
    print("Ingrese los siguientes datos para una cuenta de ahorros.")
    num_cuenta = input("Número de cuenta: ")
    tasa_interes = float(input("Tasa de interés: "))
    balance = float(input("Balance: "))

    # Crear un objeto de CuentaAhorro
    ahorros = CuentaAhorro(num_cuenta, tasa_interes, balance)

    # Obtener el número de cuenta, la tasa de interés,
    # el saldo y la fecha de vencimiento de una cuenta CD.
    print("Ingrese los siguientes datos para una CD.")
    num_cuenta = input("Número de cuenta: ")
    tasa_interes = float(input("Tasa de interés: "))
    balance = float(input("Balance: "))
    fecha_venc = input("Fecha de vencimiento: ")

    # Crear un objeto CD
    cd = CD(num_cuenta, tasa_interes, balance, fecha_venc)

    # Mostrar los datos ingresados
    print()
    print("Aquí están los datos que ingresaste")
    print()
    print("Cuenta de ahorros")
    print("------------------------")
    print(f"Número de cuenta: {ahorros.get_numero_cuenta()}")
    print(f"Tasa de interés: {ahorros.get_tasa_interes()}")
    print(f"Balance: ${ahorros.get_balance():,.2f}")

    print()
    print("CD")
    print("------------------------")
    print(f"Número de cuenta: {cd.get_numero_cuenta()}")
    print(f"Tasa de interés: {cd.get_tasa_interes()}")
    print(f"Balance: ${cd.get_balance():,.2f}")
    print(f"Fecha de vencimiento: {cd.get_fecha_vencimiento()}")


if __name__ == "__main__":
    main()
