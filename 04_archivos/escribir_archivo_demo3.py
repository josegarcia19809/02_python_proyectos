import os
import sys

nombre_archivo = input("Introduce el nombre del archivo: ")  # Nombre del archivo

# Obtener el nombre del archivo y asegurarse de que no exista.
if os.path.exists(nombre_archivo):
    print(f"El archivo {nombre_archivo} ya existe.")
    sys.exit()

num_amigos = int(input("¿Cuántos amigos tienes? "))  # Número de amigos

# Abrir el archivo.
salida_archivo = open(nombre_archivo, "w")

# Obtener los datos y escribirlos en el archivo.
for i in range(num_amigos):
    # Obtener el nombre de un amigo.
    nombre_amigo = input(f"Introduce el nombre del amigo número {i + 1}: ")
    # Escribir el nombre en el archivo.
    salida_archivo.write(nombre_amigo + "\n")

# Cerrar el archivo.
salida_archivo.close()
print("Datos grabados en el archivo.")
