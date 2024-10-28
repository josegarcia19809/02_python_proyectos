# lista_del.py

import os

os.system("clear")


def imprimir_linea():
    print("-" * 20)


# Este programa borra un elemento de una colección en un determinado índice
imprimir_linea()

numeros = [10, 20, 30, 40, 50]
print("Lista antes de borrar: ", numeros)

del numeros[2]
print("Lista después de borrar: ", numeros)
imprimir_linea()
