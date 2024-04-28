from pasajero import Pasajero

# En esta versión se usarán algoritmos de ordenamiento y búsqueda
# Se realizará por los campos clave y nombre

import os
from typing import List

# Globales
nombre_archivo: str = "pasajeros5.txt"
nombre_pagina: str = "pasajeros5.html"
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
    print("3. Ver página web")
    print("4. Ordenar por clave (burbuja)")
    print("5. Ordenar por nombre (burbuja)")
    print("6. Buscar por clave (b. binaria)")
    print("7. Buscar por nombre (b. binaria)")
    print("8. Salir")


def escribir_en_pagina_web() -> None:
    archivo = open(nombre_pagina, "w", encoding="utf-8")
    inicio: str = """
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset='utf-8'>
            <title>Registro de pasajeros</title>
            <link rel='stylesheet' href='css/bootstrap.min.css'>
        </head>
        <body>
            <div class='container'>
                <h1>Registro de pasajeros</h1>
                <table class='table table-striped'>
                    <thead>
                        <tr>
                            <th>Clave</th>
                            <th>Nombre</th>
                            <th>Origen</th>
                            <th>Destino</th>
                            <th>Pasaje</th>
                        </tr>
                    </thead>
                    <tbody>
    """  # fin de inicio
    final: str = """
                    </tbody>
                </table>
            </div>
            <script src='js/bootstrap.bundle.min.js'></script>
        </body>
    </html>
    """  # fin de final 😄

    cuerpo: str = ""
    # Se recorre el arreglo para leer todos los pasajeros
    n: int = len(listaPasajeros)
    for i in range(0, n):
        cuerpo += f"""
            <tr>
                <td>{listaPasajeros[i].clave}</td>
                <td>{listaPasajeros[i].nombre}</td>
                <td>{listaPasajeros[i].origen}</td>
                <td>{listaPasajeros[i].destino}</td>
                <td>{listaPasajeros[i].pasaje}</td>
            </tr>
        """  # fin de cuerpo
    archivo.write(inicio + cuerpo + final)
    archivo.close()


def ordenar_por_clave_burbuja() -> None:
    n: int = len(listaPasajeros)
    for i in range(0, n):
        for j in range(0, n - 1):
            if listaPasajeros[j].clave > listaPasajeros[j + 1].clave:
                aux: Pasajero = listaPasajeros[j]
                listaPasajeros[j] = listaPasajeros[j + 1]
                listaPasajeros[j + 1] = aux


def ordenar_por_nombre_burbuja() -> None:
    n: int = len(listaPasajeros)
    for i in range(0, n):
        for j in range(0, n - 1):
            if listaPasajeros[j].nombre > listaPasajeros[j + 1].nombre:
                aux: Pasajero = listaPasajeros[j]
                listaPasajeros[j] = listaPasajeros[j + 1]
                listaPasajeros[j + 1] = aux


def busqueda_binaria_por_clave(buscar: int) -> int:
    n: int = len(listaPasajeros)
    bajo: int = 0
    alto: int = n - 1
    while alto >= bajo:
        central: int = int((bajo + alto) / 2)
        if buscar > listaPasajeros[central].clave:
            bajo = central + 1
        elif buscar < listaPasajeros[central].clave:
            alto = central - 1
        else:
            return central
    return -1


def busqueda_binaria_por_nombre(buscar: str) -> int:
    n: int = len(listaPasajeros)
    bajo: int = 0
    alto: int = n - 1
    while alto >= bajo:
        central: int = int((bajo + alto) / 2)
        if buscar > listaPasajeros[central].nombre:
            bajo = central + 1
        elif buscar < listaPasajeros[central].nombre:
            alto = central - 1
        else:
            return central
    return -1


def buscar_pasajeros_por_clave() -> None:
    ordenar_por_clave_burbuja()
    clave_buscar: int = int(input("Dame clave a buscar: "))
    indice: int = busqueda_binaria_por_clave(clave_buscar)
    if indice == -1:
        print("La clave no existe...😢")
        print()
    else:
        print(f"{'CLAVE':>7}{'NOMBRE':>20}{'ORIGEN':>15}{'DESTINO':>15}{'PASAJE':>7}")
        print(listaPasajeros[indice])
        print()


def buscar_pasajeros_por_nombre() -> None:
    ordenar_por_nombre_burbuja()
    nombre_buscar: str = input("Dame nombre a buscar: ")
    indice: int = busqueda_binaria_por_nombre(nombre_buscar)
    if indice == -1:
        print("El nombre no existe...😢")
        print()
    else:
        print(f"{'CLAVE':>7}{'NOMBRE':>20}{'ORIGEN':>15}{'DESTINO':>15}{'PASAJE':>7}")
        print(listaPasajeros[indice])
        print()


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
            escribir_en_pagina_web()
            os.system(f"open {nombre_pagina}")
        elif opcion == 4:
            ordenar_por_clave_burbuja()
            mostrar_datos()
        elif opcion == 5:
            ordenar_por_nombre_burbuja()
            mostrar_datos()
        elif opcion == 6:
            buscar_pasajeros_por_clave()
        elif opcion == 7:
            buscar_pasajeros_por_nombre()
        elif opcion == 8:
            exit()
        else:
            print("Opción inexistente en el menú...")


if __name__ == '__main__':
    main()
