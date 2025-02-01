# Created by: Ing. José Luis García Morales on 30 de junio de 2020, 11:14
# Este programa es para jugar piedra, papel o tijeras.
# Al jugador se le pide que ingrese piedra, papel o tijeras.
# De manera aleatoria, el juego genera su propia respuesta.
# Poner el código para jugar aplicando las reglas del juego
# Escribir quién gana:
# "¡Es un empate!"
# "¡Gana el jugador!"
# "¡Gana la computadora!"
from random import randint

print("piedra...")
print("papel...")
print("tijeras...")

player = input("Escribe tu elección: ").lower()
rand_num = randint(0, 2)
if rand_num == 0:
    computer = "piedra"
elif rand_num == 1:
    computer = "papel"
else:
    computer = "tijeras"

print(f"Computadora dice {computer}")

# Escribe tu código aquí

