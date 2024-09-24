# El siguiente programa calcula el total de puntos ganados por un equipo de futbol
# en una serie de juegos. Permite al usuario ingresar la serie de puntos obtenidos
# de los juegos, luego -1 para señalar el final de la lista.
# Tema: valores centinela, bandera

juego = 1  # Contador de juegos
total = 0  # Total de puntos

print("Ingrese la cantidad de puntos que su equipo ha ganado "
      + "hasta ahora en la temporada, \n"
      + "luego ingrese -1 cuando haya terminado. \n")
puntos = int(input(f"Ingrese los puntos para el juego {juego}: "))

while puntos != -1:
    total = total + puntos
    juego = juego + 1
    puntos = int(input(f"Ingrese los puntos para el juego {juego}: "))

print(f"\nTotal de puntos: {total}")

# 21 23 25 30 -1
# Total: 99
