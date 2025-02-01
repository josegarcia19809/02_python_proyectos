# edad_cine.py
import os

os.system("clear")
print("Entrada al cine, solo mayores de edad")
edad = int(input("Dame tu edad: "))

if edad >= 18:
    print("Si puede pasar a ver la película")
else:
    print("No puede pasar a ver la película")
