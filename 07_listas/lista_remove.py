# lista_remove.py
import os

os.system("clear")


def imprimir_linea():
    print("-" * 20)


# Programa que sirve para remover un elemento de una colección
imprimir_linea()
# Crear una lista de colores y mostrar
colores = ["rojo", "azul", "verde", "amarillo"]
print("Lista original", colores)

# Preguntar cuál color quiero remover
elemento = input("Dime elemento a remover: ")
try:
    colores.remove(elemento)
    print("Lista modificada", colores)
except ValueError:
    print("El elemento no se encontró en la lista")
