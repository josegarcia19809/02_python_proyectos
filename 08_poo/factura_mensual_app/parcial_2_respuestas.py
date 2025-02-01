from factura_mensual import FacturaMensual


def main():
    for no_lista in range(1, 19):
        print("-" * 25, "Num. de lista: ", no_lista)
        no_paquete = (no_lista % 3) + 1
        minutos = no_lista * 40
        factura = FacturaMensual(no_paquete, minutos)
        cargo = factura.cargos_totales()
        print(f"no_paquete: {no_paquete}")
        print(f"minutos: {minutos}")
        print(f"Cargo: {cargo}")
        print("-" * 100)
        print()


if __name__ == '__main__':
    main()
