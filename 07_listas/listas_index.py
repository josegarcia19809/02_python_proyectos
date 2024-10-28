# listas_index.py
import os

os.system("clear")
# Este programa demostrará cómo localizar el índice de un elemento a buscar.
# Si lo encuentra, reemplazará al elemento

# Crear lista de algunos alimentos
alimentos = ["Pizza", "Hamburguesa", "Papas"]

# Mostramos la lista
print(alimentos)

# Pedir el elemento a cambiar
elemento = input("Dime el elemento a cambiar: ")

try:
    # Busca el elemento y obtiene el índice
    indice = alimentos.index(elemento)
    # Si lo encuentra, pide el nuevo elemento
    nuevo_elemento = input("Dame el nuevo elemento: ")
    # Reemplazar el antiguo elemento por el nuevo
    alimentos[indice] = nuevo_elemento

    print("Lista actualizada de alimentos")
    print(alimentos)
except ValueError:
    print("El elemento no se encontró en la lista de alimentos")
