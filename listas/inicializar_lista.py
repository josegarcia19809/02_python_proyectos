# inicializar_lista con ceros

from typing import List

N: int = 10


def inicializar_lista() -> List[int]:
    nueva_lista: List[int] = []
    for i in range(N):
        nueva_lista.append(0)
    return nueva_lista


def imprimir_lista(lista: List[int]) -> None:
    for i in range(N):
        print(f"{lista[i]}", end=" ")
    print()


numeros: List[int] = inicializar_lista()
imprimir_lista(numeros)
