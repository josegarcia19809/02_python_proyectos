def descontar_10_por_ciento(precio_original):
    descuento = precio_original * 0.10
    precio_con_descuento = precio_original - descuento
    print(f"El precio con descuento es de {precio_con_descuento}")


def main():
    print("PROGRAMA PARA CALCULAR UN DESCUENTO DEL 10% A UN PRODUCTO")
    precio_inicial = float(input("Dime el precio del producto: "))
    descontar_10_por_ciento(precio_inicial)


main()
