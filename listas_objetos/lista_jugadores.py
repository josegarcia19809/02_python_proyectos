class Jugador:
    def __init__(self, nombre, goles):
        self.nombre = nombre
        self.goles = goles

    def __str__(self):
        return f"Nombre: {self.nombre}, goles: {self.goles}"


if __name__ == "__main__":
    # Crear una lista que se llame equipo para guardar Jugadores
    equipo = []

    # Agregar un jugador
    equipo.append(Jugador("Messi", 25))

    # Agregar otro jugador usando una variable
    j1 = Jugador("Alan", 1)
    equipo.append(j1)

    print("-"*100)
    print("Jugadores:")
    for i in range(len(equipo)):
        print(equipo[i])

    print("-"*100)
    # for mejorado
    print("Jugadores:")
    for jugador in equipo:
        print(jugador)
