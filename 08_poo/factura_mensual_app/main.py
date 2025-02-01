from factura_mensual import FacturaMensual


def main():
    no_lista = 1
    no_paquete = (no_lista % 3) + 1
    minutos = no_lista * 40
    factura = FacturaMensual(no_paquete, minutos)
    cargo = factura.cargos_totales()
    print(cargo)


if __name__ == '__main__':
    main()
