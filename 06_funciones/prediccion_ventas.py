# prediccion_ventas.py

# La división de ventas Este genera el 60% de las ventas.
# La Oeste genera el 20%
# La Norte genera el 10%
# La Sur genera el 10%

# Basándose en esos porcentajes escribe 4 funciones que muestren lo que venderá cada
# división este año. Se proyecta una venta total de $200,000

def calcular_ventas_este(ventas_totales: float):
    ventas_este = ventas_totales * 0.60
    print(f"Ventas Este: {ventas_este}")


def calcular_ventas_oeste(ventas_totales: float):
    ventas_oeste = ventas_totales * 0.20
    print(f"Ventas Oeste: {ventas_oeste}")


def calcular_ventas_norte(ventas_totales: float):
    ventas_norte = ventas_totales * 0.60
    print(f"Ventas Norte: {ventas_norte}")


def calcular_ventas_sur(ventas_totales: float):
    ventas_sur = ventas_totales * 0.60
    print(f"Ventas Sur: {ventas_sur}")


def main():
    calcular_ventas_este(200000)
    calcular_ventas_oeste(200000)
    calcular_ventas_norte(200000)
    calcular_ventas_sur(200000)


main()
