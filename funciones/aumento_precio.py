"""
Elaborado por José L. García: lunes 3 de mayo de 2024
Este programa calcula el precio minorista de un producto
Nombre: aumento_precio
"""


def calcular_precio_venta(costo_mayorista: float, porcentaje_aumento: int) -> float:
    costo_minorista: float = costo_mayorista + (
        costo_mayorista * porcentaje_aumento / 100)
    return costo_minorista


def main():
    print("Dame el precio del producto al mayoreo: ", end="")
    precio_al_mayoreo: float = float(input())

    # Validar la entrada
    while precio_al_mayoreo < 0:
        print("Entrada no válida. Debe ser positivo")
        print("Introduzca nuevamente el precio: ", end="")
        precio_al_mayoreo = float(input())

    print("Dame porcentaje de aumento para venta al menudeo: ", end="")
    porcentaje_de_aumento: int = int(input())

    # Validar
    while porcentaje_de_aumento < 0:
        print("Entrada no válida. Debe ser positivo")
        print("Introduzca nuevamente el porcentaje: ", end="")
        porcentaje_de_aumento = int(input())

    # Calcular precio al menudeo
    precio_menudeo: float = calcular_precio_venta(precio_al_mayoreo,
                                                  porcentaje_de_aumento)

    print(f"El precio al menudeo es de ${precio_menudeo:.2f}")


if __name__ == "__main__":
    main()
