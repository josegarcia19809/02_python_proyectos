from pasajero import Pasajero

# Global
pasajeroX: Pasajero


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
    pedir_datos()
    mostrar_datos()


if __name__ == '__main__':
    main()
