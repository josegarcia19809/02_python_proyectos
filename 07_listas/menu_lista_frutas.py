# menu_lista_frutas.py
import os

os.system("clear")
frutas = ["manzana", "pera", "piña", "naranja", "lima"]


def menu():
    print("-" * 30)
    print("Uso de una lista de frutas")
    print("1. Añadir una fruta")
    print("2. Mostrar lista frutas")
    print("3. Buscar una fruta")
    print("4. Borrar una fruta")
    print("5. Cambiar una fruta")
    print("6. Salir")


def meter_fruta():
    nombre_fruta = input("Dame el nombre de una fruta: ")
    frutas.append(nombre_fruta)


def mostrar_lista_frutas():
    print("Lista de frutas")
    for fruta in sorted(frutas):
        print(fruta)


def buscar_fruta(nombre_fruta: str) -> int:
    try:
        return frutas.index(nombre_fruta)
    except ValueError:
        return -1


def buscar_fruta_por_nombre():
    nombre_fruta = input("Dame nombre de fruta a buscar:")
    indice = buscar_fruta(nombre_fruta)
    if indice != -1:
        print(f"La fruta está en el índice {indice}")
    else:
        print("El nombre de la fruta no existe")


def borrar_fruta():
    nombre_fruta = input("Dame nombre de fruta a borrar:")
    if nombre_fruta in frutas:
        frutas.remove(nombre_fruta)
    else:
        print("El nombre de la fruta no existe")


def cambiar_nombre_fruta():
    nombre_fruta = input("Dame nombre de fruta a cambiar:")
    indice = buscar_fruta(nombre_fruta)
    if indice != -1:
        nuevo_nombre_fruta = input("Dame nuevo nombre:")
        frutas[indice] = nuevo_nombre_fruta
        print("Nombre cambiado")
    else:
        print("El nombre de la fruta no existe")


def main():
    opcion = 0
    while opcion != 6:
        menu()
        opcion = int(input("Elige la opción: "))
        if opcion == 1:
            meter_fruta()
        elif opcion == 2:
            mostrar_lista_frutas()
        elif opcion == 3:
            buscar_fruta_por_nombre()
        elif opcion == 4:
            borrar_fruta()
        elif opcion == 5:
            cambiar_nombre_fruta()
        elif opcion == 6:
            print("Saliendo...")
        else:
            print("Opción no válida")


# Ejecuta el programa
main()
