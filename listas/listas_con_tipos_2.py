# listas_con_tipos_2
from typing import List

N: int = 8  # tamaño de la lista


def imprimir_lista(lista: List[float]) -> None:
    for i in range(0, N):
        print(lista[i], end=' ')
    print()


x: List[float] = [14.0, 12.0, 8.0, 7.0, 6.41, 5.23, 6.15, 7.25]
imprimir_lista(x)

# Cambiar el elemento [4] a 45 e imprimir la lista
x[4] = 45
imprimir_lista(x)

# Añadir al elemento [5] 3.5 unidades e imprimir la lista
x[5] = x[5] + 3.5
imprimir_lista(x)

# Modificar el elemento [6], que sea la suma de los elementos [1] y [2]
# e imprimir la lista
x[6] = x[1] + x[2]
imprimir_lista(x)
