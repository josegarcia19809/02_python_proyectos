from cargos_bancarios import CargosBancarios


def main():
    print("Cargos bancarios")
    saldo = float(input("Dame saldo del cliente: "))
    cheques = int(input("Dame cantidad de cheques emitidos: "))
    cargos_b = CargosBancarios(saldo=saldo, cheques=cheques)
    while True:
        menu()
        opcion = int(input("Dame tu opción: "))
        if opcion == 1:
            print(f"Saldo actual: {cargos_b.obtener_saldo_actual()}")
        elif opcion == 2:
            print(f"Cargos bancarios: {cargos_b.obtener_cobro_total()}")
            print(f"Saldo después de los cobros: {cargos_b.obtener_saldo_actual()}")
        elif opcion == 3:
            print("Actualizar datos")
            saldo = float(input("Dame nuevo saldo del cliente: "))
            cheques = int(input("Dame nueva cantidad de cheques emitidos: "))
            cargos_b = CargosBancarios(saldo=saldo, cheques=cheques)
        elif opcion == 4:
            break
        else:
            print("Opción no valida")


def menu():
    print("----------------------------------------------------")
    print("Menú principal")
    print("1.- Mostrar saldo actual")
    print("2.- Aplicar cargos bancarios y mostrar el saldo restante")
    print("3.- Asignar nuevos valores al balance de la cuenta")
    print("4.- Salir")


if __name__ == '__main__':
    main()
