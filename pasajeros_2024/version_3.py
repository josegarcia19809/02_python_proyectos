from pasajero import Pasajero

import os
from typing import List

# Globales
nombre_archivo: str = "pasajeros3.txt"
listaPasajeros: List['Pasajero'] = []


def verificar_archivo() -> None:
    if not os.path.isfile(nombre_archivo):
        print("El archivo no existe, se creará uno con ese nombre")
        crear_archivo = open(nombre_archivo, "w", encoding="utf-8")
        crear_archivo.close()


def escribir_en_archivo() -> None:
    archivo = open(nombre_archivo, "w", encoding="utf-8")
    for aux in listaPasajeros:
        if aux.clave == 0:
            continue
        archivo.write(f"{aux.clave}|{aux.nombre}|")
        archivo.write(f"{aux.origen}|{aux.destino}|")
        archivo.write(f"{aux.pasaje}\n")
    archivo.close()


def leer_archivo() -> None:
    archivo = open(nombre_archivo, "r")
    for linea in archivo.readlines():
        registro = linea.split("|")  # dividir mediante el separador |
        clave: int = int(registro[0])
        nombre: str = registro[1]
        origen: str = registro[2]
        destino: str = registro[3]
        pasaje: float = float(registro[4])
        insertar(clave, nombre, origen, destino, pasaje)
    archivo.close()
    # fin de leer_archivo


def insertar(clavex: int, nombrex: str, origenx: str, destinox: str,
             pasajex: float) -> None:
    pasajeroX: Pasajero = Pasajero(clavex, nombrex, origenx, destinox, pasajex)
    listaPasajeros.append(pasajeroX)
    # fin de insertar


def pedir_datos() -> None:
    print("Ingresa los datos del pasajero")
    clave: int = int(input("Dame clave: "))
    nombre: str = input("Dame nombre: ")
    origen: str = input("Dame origen: ")
    destino: str = input("Dame destino: ")
    pasaje: float = float(input("Dame pasaje: "))
    insertar(clave, nombre, origen, destino, pasaje)
    escribir_en_archivo()
    # fin  de pedir_datos


def mostrar_datos() -> None:
    print(f"{'CLAVE':>7}{'NOMBRE':>20}{'ORIGEN':>15}{'DESTINO':>15}{'PASAJE':>7}")
    for pasajero in listaPasajeros:
        print(pasajero)
    # fin de mostrar_datos


def menu() -> None:
    print("\nVIAJES A TODO EL MUNDO")
    print("\t:: Elige tu opción :: ")
    print("1. Alta de pasajeros")
    print("2. Reporte general")
    print("3. Salir")


def main() -> None:
    # Operaciones para el pasajero
    verificar_archivo()
    leer_archivo()
    while True:
        menu()
        opcion: int = int(input("Elige: "))
        if opcion == 1:
            pedir_datos()
            mostrar_datos()
        elif opcion == 2:
            mostrar_datos()
        elif opcion == 3:
            print("Saliendo...")
            exit()
        else:
            print("Opción no válida")


if __name__ == '__main__':
    main()
