# busqueda_binaria

from typing import List


def busqueda_binaria(valores: List[int], valor_a_buscar: int) -> int:
    bajo: int = 0
    alto: int = len(valores) - 1

    while bajo <= alto:
        mitad: int = (bajo + alto) // 2
        buscando: int = valores[mitad]
        if buscando == valor_a_buscar:
            return mitad
        elif buscando > valor_a_buscar:
            alto = mitad - 1
        else:
            bajo = mitad + 1
    return -1


# Ejemplo de uso
arreglo: List[int] = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
valor: int = int(input("Ingresa número a buscar: "))
indice: int = busqueda_binaria(arreglo, valor)
if indice != -1:
    print(f"El valor {valor} fue encontrado en la posición {indice}")
else:
    print(f"El valor {valor} no fue encontrado en la lista")
