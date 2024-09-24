juego = 1  # Contador de juegos
total = 0  # Total de puntos

print("Ingrese la cantidad de puntos que su equipo ha ganado "
      + "hasta ahora en la temporada, \n"
      + "luego ingrese -1 cuando haya terminado. \n")
puntos = int(input(f"Ingrese los puntos para el juego {juego}: "))

while True:
    total = total + puntos
    juego = juego + 1
    puntos = int(input(f"Ingrese los puntos para el juego {juego}: "))
    if puntos == -1:
        break

print(f"\nTotal de puntos: {total}")
