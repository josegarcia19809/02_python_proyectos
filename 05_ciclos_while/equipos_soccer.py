# equipos_soccer.py


JUGADORES_MIN = 9  # En mayúsculas porque es un valor constante
JUGADORES_MAX = 15

jugadores_por_equipo = int(input("Ingresa el número de jugadores por equipo: "))

# Validar que los jugadores por equipo no sea menor al mínimo requerido
# ni mayor al máximo permitido
while jugadores_por_equipo < JUGADORES_MIN or jugadores_por_equipo > JUGADORES_MAX:
    print(f"Número mínimo de jugadores: {JUGADORES_MIN}")
    print(f"Número máximo de jugadores: {JUGADORES_MAX}")
    jugadores_por_equipo = int(
        input("Ingresa nuevamente el número de jugadores por equipo: ")
        )

jugadores_disponibles = int(input("Ingresa número de jugadores disponibles: "))

while jugadores_disponibles < 0:
    print("La cantidad debe ser 0 o más")
    jugadores_disponibles = int(
        input("Ingresa número de jugadores disponibles nuevamente: ")
    )

# Calcular el número de equipos
equipos = jugadores_disponibles // jugadores_por_equipo
jugadores_sobrantes = jugadores_disponibles % jugadores_por_equipo

print(f"Se forman {equipos} equipos y sobraran {jugadores_sobrantes} jugadores")
