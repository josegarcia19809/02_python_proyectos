"""
 Elaborado por José L. García: lunes 3 de junio de 2024
 Este programa muestra la división que obtuvo las mayores ventas trimestrales
 Nombre: division ganadora
"""


def obtener_ventas(nombre_division: str) -> float:
    print(f"Escribe las ventas trimestrales de la división {nombre_division}: ", end="")
    ventas: float = float(input())

    # Validar
    while ventas < 0:
        print("Escribe un valor positivo: ", end="")
        ventas: float = float(input())

    return ventas


def encontrar_mayor(ventas_norte: float, ventas_sur: float, ventas_este: float,
                    ventas_oeste: float) -> None:
    division_ganadora: str = "Norte"
    venta_mayor: float = ventas_norte

    if ventas_sur > venta_mayor:
        division_ganadora = "Sur"
        venta_mayor = ventas_sur

    if ventas_este > venta_mayor:
        division_ganadora = "Este"
        venta_mayor = ventas_este

    if ventas_oeste > venta_mayor:
        division_ganadora = "Oeste"
        venta_mayor = ventas_oeste

    print(f"La división ganadora es {division_ganadora} con ventas de ${venta_mayor:.2f}")


def main():
    ventas_norte: float = obtener_ventas("Norte")
    ventas_sur: float = obtener_ventas("Sur")
    ventas_este: float = obtener_ventas("Este")
    ventas_oeste: float = obtener_ventas("Oeste")

    encontrar_mayor(ventas_norte, ventas_sur, ventas_este, ventas_oeste)


if __name__ == "__main__":
    print("-" * 100)
    main()
