# Este programa calcula el número total de puntos que un equipo de futbol
# ha ganado en una serie de juegos.
# El usuario ingresa una serie de valores de puntos, luego -1 al finalizar

juego = 1  # Contador de juegos
total = 0  # Acumulador

print("Ingrese la cantidad de puntos que su equipo ha ganado " +
      "hasta ahora en la temporada, \n" +
      "luego ingrese -1 cuando haya terminado. \n")

puntos = int(input(f"Ingrese los puntos para el juego {juego}: "))

while puntos != -1:
    total = total + puntos
    juego = juego + 1
    puntos = int(input(f"Ingrese los puntos para el juego {juego}: "))

print(f"\nTotal de puntos: {total}")
