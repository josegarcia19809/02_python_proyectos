from pasajero import Pasajero

import os

# Guardar los datos que se han pedido en un archivo de texto
# Posteriormente se van a recuperar

# Global
pasajeroX: Pasajero
nombre_archivo = "pasajeros2.txt"


def verificar_archivo():
    if not os.path.isfile(nombre_archivo):
        print("El archivo no existe, se creará uno con ese nombre")
        crear_archivo = open(nombre_archivo, "w", encoding="utf-8")
        crear_archivo.close()


def escribir_en_archivo():
    archivo = open(nombre_archivo, "w", encoding="utf-8")
    archivo.write(f"{pasajeroX.clave}|{pasajeroX.nombre}|")
    archivo.write(f"{pasajeroX.origen}|{pasajeroX.destino}|{pasajeroX.pasaje}")
    archivo.close()


def leer_archivo():
    archivo = open(nombre_archivo, "r")
    for linea in archivo.readlines():
        registro = linea.split("|")
        clave = int(registro[0])
        nombre = registro[1]
        origen = registro[2]
        destino = registro[3]
        pasaje = float(registro[4])
        insertar(clave, nombre, origen, destino, pasaje)
    archivo.close()
    # fin de leer_archivo


def insertar(clavex: int, nombrex: str, origenx: str, destinox: str,
             pasajex: float) -> None:
    global pasajeroX
    pasajeroX = Pasajero(clavex, nombrex, origenx, destinox, pasajex)
    # fin de insertar


def pedir_datos() -> None:
    print("Ingresa los datos del pasajero")
    clave: int = int(input("Dame clave: "))
    nombre: str = input("Dame nombre: ")
    origen: str = input("Dame origen: ")
    destino: str = input("Dame destino: ")
    pasaje: float = float(input("Dame pasaje: "))
    insertar(clave, nombre, origen, destino, pasaje)
    # fin  de pedir_datos


def mostrar_datos() -> None:
    print(f"{'CLAVE':>7}{'NOMBRE':>20}{'ORIGEN':>15}{'DESTINO':>15}{'PASAJE':>7}")
    print(pasajeroX)
    # fin de mostrar_datos


def main() -> None:
    verificar_archivo()
    leer_archivo()
    mostrar_datos()
    # pedir_datos()
    # escribir_en_archivo()
    # print("Guardado")


if __name__ == '__main__':
    main()
