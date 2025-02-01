# Este programa calcula el total de ventas de acuerdo a la cantidad de boletos
# vendidos en un estadio

print("-" * 100)


def ingresos_boletos_a(boletos_vendidos):
    precio_boleto_a = 20
    ingresos = boletos_vendidos * precio_boleto_a
    return ingresos


def ingresos_boletos_b(boletos_vendidos):
    precio_boleto_b = 15
    ingresos = boletos_vendidos * precio_boleto_b
    return ingresos


def ingresos_boletos_c(boletos_vendidos):
    precio_boleto_c = 10
    ingresos = boletos_vendidos * precio_boleto_c
    return ingresos


def main():
    boletos_a = int(input("Cantidad de boletos vendidos en clase A: "))
    ventas_boletos_a = ingresos_boletos_a(boletos_a)

    boletos_b = int(input("Cantidad de boletos vendidos en clase B: "))
    ventas_boletos_b = ingresos_boletos_b(boletos_b)

    boletos_c = int(input("Cantidad de boletos vendidos en clase C: "))
    ventas_boletos_c = ingresos_boletos_c(boletos_c)

    total_ingresos = ventas_boletos_a + ventas_boletos_b + ventas_boletos_c
    print(f"Total de la venta de boletos: ${total_ingresos:,.2f}")


main()
