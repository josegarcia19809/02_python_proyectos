from cuenta_ahorros import CuentaAhorro

print("-"*100)
def main():
    mi_cuenta = CuentaAhorro(5000)
    print(mi_cuenta)
    mi_cuenta.sacar_dinero(1000)
    print(mi_cuenta)
    mi_cuenta.sacar_dinero(3000)
    print(mi_cuenta)
    mi_cuenta.sacar_dinero(2000)
    print(mi_cuenta)


if __name__ == '__main__':
    main()
