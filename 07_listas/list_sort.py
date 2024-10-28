# list_sort.py


def imprimir_linea():
    print("-" * 20)


# Este programa sirve para utilizar un método para ordenar los elementos de una lista
imprimir_linea()

mi_lista = [9, 1, 0, 2, 8, 6, 7, 4, 5, 3]
print("Orden original: ", mi_lista)

# Ordenar y mostrar
mi_lista.sort()
print("Ordenados", mi_lista)
imprimir_linea()

nombres = ["Veronica", "Lucia", "Lucero", "Juan", "zod", "ariana"]
print("Lista original: ", nombres)
imprimir_linea()
nombres.sort()
print("Lista ordenada: ", nombres)
imprimir_linea()
