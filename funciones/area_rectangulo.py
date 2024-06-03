"""
 Elaborado por José L. García: viernes 24 de mayo de 2024
 Este programa calcula el área de un rectángulo
 Nombre: area_rectangulo
"""


def obtener_largo() -> float:
    print("Escribe el largo del rectángulo: ", end="")
    largo: float = float(input())
    return largo


def obtener_ancho() -> float:
    print("Escribe el ancho del rectángulo: ", end="")
    ancho: float = float(input())
    return ancho


def calcular_area(largura: float, anchura: float) -> float:
    return largura * anchura


def mostrar_datos(largura: float, anchura: float, area: float) -> None:
    print(f"El rectángulo con largura {largura} y anchura {anchura} "
          f"tiene {area} unidades cuadradas")


def main():
    largo: float = obtener_largo()
    ancho: float = obtener_ancho()
    area: float = calcular_area(largura=largo, anchura=ancho)
    mostrar_datos(largo, ancho, area)


if __name__ == "__main__":
    main()
