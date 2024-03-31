import os

# Obtener el nombre del archivo
nombre_archivo = input("Introduce el nombre del archivo: ")

# Abrir el archivo
with open(nombre_archivo, 'r') as archivo:
    # Leer la primera línea del archivo
    linea = archivo.readline()

    # Desplegar la línea
    print("La primera línea del archivo es:")
    print(linea)
