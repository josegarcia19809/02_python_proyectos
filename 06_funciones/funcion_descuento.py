# funcion_descuento.py

# debe llevar 2 funciones: main, calcular_descuento. La función calcular_descuento debe
# recibir 2 valores, una variable servirá para guardar la cantidad a pagar; y, la otra
# para el porcentaje de descuento. Debe mostrar el descuento
# calcular_descuento(1000, 15) => "El descuento es de 150 pesos"


def calcular_descuento(cantidad: float, porcentaje: int):
    descuento = cantidad * porcentaje / 100.0
    print(f"El descuento es de {descuento:.2f} pesos ")


def main():
    calcular_descuento(1000, 15)


main()
