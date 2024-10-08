# gastos_papeleria.py
# import os
#
# os.system("clear")


# Una papelería vende lapices a $4.00 cada uno; gomas, a $2.50; y brujulas, a $12.00.
# Escribe 3 funciones para calcular el gasto de cada artículo.
# Cada función preguntará la cantidad y mostrará el total de ese artículo

def imprimir_linea():
    print("-" * 50)


def cobrar_venta_lapices():
    precio_lapiz = 4.00
    cantidad = int(input("¿Cuántos lapices quieres? "))

    total_venta = precio_lapiz * cantidad
    print(f"Cobro de lápices: {total_venta}")
    imprimir_linea()


def cobrar_venta_gomas():
    precio_goma = 2.50
    cantidad = int(input("¿Cuántas gomas quieres? "))

    total_ventas = precio_goma * cantidad
    print(f"Cobro de gomas: {total_ventas}")
    imprimir_linea()


def cobrar_venta_brujulas():
    precio_brujula = 12.00
    cantidad = int(input("¿Cuántas brujulas quieres? "))

    total_ventas = precio_brujula * cantidad
    print(f"Cobro de brujulas: {total_ventas}")
    imprimir_linea()


def main():
    cobrar_venta_lapices()
    cobrar_venta_gomas()
    cobrar_venta_brujulas()


main()
