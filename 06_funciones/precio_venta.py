# precio_venta.py

# Supón que te piden que diseñes un programa que calcule el precio de venta de un
# artículo en un comercio minorista, cuyo porcentaje de descuento es del 20%.
# Deben declarar funciones para obtener el precio regular, calcular el descuento y la
# función principal.

PORCENTAJE_DESCUENTO = 0.20


def obtener_precio_regular() -> float:
    precio = float(input("Dame el precio regular del producto: "))
    return precio


def calcular_descuento(precio: float) -> float:
    return precio * PORCENTAJE_DESCUENTO


def main():
    precio_regular = obtener_precio_regular()
    descuento = calcular_descuento(precio_regular)
    precio_venta = precio_regular - descuento

    print(f"El precio de venta es ${precio_venta: .2f}.")


main()
