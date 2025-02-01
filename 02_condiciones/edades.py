# edades.py
import sys

edad = int(input("Dame tu edad: "))

if edad < 0:
    print("Edad no válida")
    print("Vuelva a ejecutar el programa")
    sys.exit(1)

print("Entraste. La edad es válida")
