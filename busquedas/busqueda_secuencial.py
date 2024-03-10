# busqueda_secuencial
from typing import List


def buscar(valor_a_buscar: int, lista_numeros: List[int]) -> int:
    for i in range(len(lista_numeros)):
        if valor_a_buscar == lista_numeros[i]:
            return i
    return -1  # Si no lo encuentra


edades: List[int] = [23, 57, 87, 12, 60, 45, 11, 15, 99, 65, 2, 43]

opcion: int = 0
while opcion != 2:
    print()
    print("---------------------")
    print("Búsqueda secuencial")
    print("1.- Buscar número")
    print("2.- Salir")
    opcion = int(input("?: "))
    if opcion == 1:
        numero_a_buscar: int = int(input("Ingrese número a buscar: "))

        indice: int = buscar(numero_a_buscar, edades)

        if indice == -1:
            print("No se encontró")
        else:
            print(f"Se encontró en la posición {indice}")

    elif opcion != 2:
        print("Opción no válida")
