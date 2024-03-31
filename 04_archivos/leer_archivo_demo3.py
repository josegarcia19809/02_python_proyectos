import os

# Obtener el nombre del archivo
nombre_archivo = input("Dame el nombre del archivo: ")

# Asegurarse de que el archivo exista
if not os.path.exists(nombre_archivo):
    print("El archivo", nombre_archivo, "no existe")
    exit(0)

# Abrir el archivo
archivo = open(nombre_archivo, 'r')

# Leer el archivo
linea = archivo.readline()
print("La primer línea dice:")
print(linea)

# Cerrar el archivo
archivo.close()
