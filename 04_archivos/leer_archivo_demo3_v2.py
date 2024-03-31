import os

# Obtener el nombre del archivo
nombre_archivo = input("Dame el nombre del archivo: ")

# Verificar si el archivo existe
if not os.path.exists(nombre_archivo):
    print("El archivo", nombre_archivo, "no existe")
    exit(0)

# Abrir el archivo y leer la primera línea
with open(nombre_archivo, 'r') as archivo:
    # Leer la primera línea del archivo
    linea = archivo.readline()

    # Desplegar la línea
    print("La primer línea dice:")
    print(linea)
