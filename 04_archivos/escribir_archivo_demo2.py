nombreArchivo = input("Introduce el nombre del archivo: ")  # Nombre del archivo
numAmigos = int(input("¿Cuántos amigos tienes? "))  # Número de amigos

# Abrir el archivo.
salidaArchivo = open(nombreArchivo, "w")

# Obtener los datos y escribirlos en el archivo.
for i in range(numAmigos):
    # Obtener el nombre de un amigo.
    nombreAmigo = input(f"Introduce el nombre del amigo número {i + 1}: ")
    # Escribir el nombre en el archivo.
    salidaArchivo.write(nombreAmigo + "\n")

# Cerrar el archivo.
salidaArchivo.close()
print("Datos grabados en el archivo.")
