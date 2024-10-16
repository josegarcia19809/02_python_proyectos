def calcular_precio_con_descuento(precio_original: float, descuento: int) -> float:
    descuento_producto = precio_original * (descuento / 100.00)
    precio_con_descuento = precio_original - descuento_producto
    return precio_con_descuento


def main():
    print("Programa para calcular el precio de un producto con descuento")
    precio = float(input("Dame el precio del producto: "))
    descuento = int(input("Dame el porcentaje de descuento: "))
    precio_final = calcular_precio_con_descuento(precio, descuento)
    print(f"El precio con descuento es de ${precio_final:,.2f}")


main()
