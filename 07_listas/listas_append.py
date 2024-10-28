# listas_append.py
import os

os.system("clear")
# Este programa demuestra cómo anexar elementos al final de una lista

# Crear una lista vacía
lista_nombres = []

# Crear una variable para controlar el bucle
repetir = 's'

# Añadir nombres a la lista  
while repetir == 's':
    # Pedir al usuario un nombre
    nombre = input("Ingresa un nombre: ")
    # Anexamos el nombre a la lista
    lista_nombres.append(nombre)

    print("¿Deseas ingresar otro nombre?")
    repetir = input("s=si, cualquier otra letra = no: ")
    print()

# Mostrar los nombres de la lista
print("Aqui están los nombres que se ingresaron:")
for nombre in lista_nombres:
    print(nombre)
