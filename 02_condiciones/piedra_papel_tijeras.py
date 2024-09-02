# Creado por José L. García 2 de septiembre 2024
# Este programa simula el juego de piedra, papel o tijeras

from random import randint

print("piedra...")
print("papel...")
print("tijeras...")

player = input("Escribe tu elección: ").lower()
rand_num = randint(0, 2) # 0 1 2

if rand_num == 0:
    computer = "piedra"
elif rand_num == 1:
    computer = "papel"
else:
    computer = "tijeras"
    
print(f"Computadora dice {computer}")

if player == computer:
    print("Empate!!!")

elif player == "tijeras":
    if computer == "papel":
        print("Gana el jugador")
    else:
        print("Gana la computadora")

elif player == "papel":
    if computer == "piedra":
        print("Gana el jugador")
    else:
        print("Gana la computadora")
        
elif player == "piedra":
    if computer == "tijeras":
        print("Gana el jugador")
    else:
        print("Gana la computadora")
else:
    print("Opción no válida")
