from typing import List


class Jugador:
    def __init__(self, numero: int, nombre: str, posicion: str, goles: int) -> None:
        self.numero: int = numero
        self.nombre: str = nombre
        self.posicion: str = posicion
        self.goles: int = goles

    def __str__(self):
        return (f"{self.numero:>7} {self.nombre:>25} {self.posicion:>15}"
                f" {self.goles:>5}")


def imprimir_lista_jugadores(jugadores: List[Jugador]) -> None:
    print("Jugadores:")
    print(f"{'numero':>7} {'nombre':>25} {'posicion':>15}"
          f" {'goles':>5}")
    for jugador in jugadores:
        print(jugador)


def imprimir_delanteros(jugadores: List[Jugador]) -> None:
    print(f"{'numero':>7} {'nombre':>25} {'posicion':>15}"
          f" {'goles':>5}")
    print("-" * 60)
    for jugador in jugadores:
        if jugador.posicion == "Delantero":
            print(jugador)


def imprimir_goleadores(jugadores: List[Jugador]) -> None:
    print(f"{'numero':>7} {'nombre':>25} {'posicion':>15}"
          f" {'goles':>5}")
    print("-" * 60)
    for jugador in jugadores:
        if jugador.goles > 8:
            print(jugador)


def obtener_cantidad_jugadores_segun_posicion(jugadores: List[Jugador], posicion: str) \
    -> int:
    total_jugadores: int = 0
    for jugador in jugadores:
        if jugador.posicion == posicion:
            total_jugadores += 1
    return total_jugadores


def obtener_cantidad_goles_segun_posicion(jugadores: List[Jugador], posicion: str) \
    -> int:
    total_goles: int = 0
    for jugador in jugadores:
        if jugador.posicion == posicion:
            total_goles += jugador.goles
    return total_goles


def obtener_promedio_goles_segun_posicion(jugadores: List[Jugador], posicion: str) -> \
    float:
    total_goles: int = 0
    total_jugadores: int = 0
    for jugador in jugadores:
        if jugador.posicion == posicion:
            total_goles += jugador.goles
            total_jugadores += 1
    if total_jugadores == 0:
        return 0.0
    else:
        return total_goles / total_jugadores


def main():
    # Crear una lista que se llame equipo para guardar Jugadores
    equipo: List[Jugador] = []
    # Agregar jugadores

    # Jugadores delanteros
    equipo.append(Jugador(1, "Lionel Messi", "Delantero", 10))
    equipo.append(Jugador(9, "Cristiano Ronaldo", "Delantero", 12))
    equipo.append(Jugador(10, "Neymar Jr.", "Delantero", 8))
    equipo.append(Jugador(7, "Kylian Mbappé", "Delantero", 9))

    # Jugadores mediocampistas
    equipo.append(Jugador(8, "Kevin De Bruyne", "Mediocampista", 5))
    equipo.append(Jugador(6, "Luka Modric", "Mediocampista", 13))
    equipo.append(Jugador(5, "N'Golo Kanté", "Mediocampista", 2))
    equipo.append(Jugador(14, "Frenkie de Jong", "Mediocampista", 4))
    equipo.append(Jugador(20, "Toni Kroos", "Mediocampista", 4))

    # Jugadores defensores
    equipo.append(Jugador(4, "Virgil van Dijk", "Defensor", 1))
    equipo.append(Jugador(3, "Sergio Ramos", "Defensor", 2))
    equipo.append(Jugador(22, "Marquinhos", "Defensor", 1))

    print("-" * 100)
    imprimir_lista_jugadores(equipo)

    # Delanteros
    print("-" * 100)
    imprimir_delanteros(equipo)

    print("-" * 100)
    imprimir_goleadores(equipo)

    print("-" * 100)
    posicion: str
    posicion = "Defensor"
    cantidad: int = obtener_cantidad_jugadores_segun_posicion(equipo, posicion)
    print(f"Total de jugadores en la posición {posicion}: {cantidad}")

    print("-" * 100)
    cantidad_goles: int = obtener_cantidad_goles_segun_posicion(equipo, posicion)
    print(f"Total de goles en la posición {posicion}: {cantidad_goles}")

    print("-" * 100)
    posicion = "Defensor"
    promedio_goles: float = obtener_promedio_goles_segun_posicion(equipo, posicion)
    print(f"Promedio de goles en la posición {posicion}: {promedio_goles:>.1f}")


if __name__ == "__main__":
    main()
