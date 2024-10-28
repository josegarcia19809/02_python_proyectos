def imprimir_linea():
    print("-" * 20)


# Este programa sirve para utilizar un método para invertir los elementos de una lista
imprimir_linea()

mi_lista = [9, 1, 0, 2, 8, 6, 7, 4, 5, 3]
print("Orden original: ", mi_lista)

# Invertir y mostrar
imprimir_linea()
mi_lista.reverse()
print("Invertidos", mi_lista)
imprimir_linea()
