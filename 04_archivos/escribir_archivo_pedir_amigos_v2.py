amigos = int(input("¿Cuántos amigos tienes? "))

# Abrir el archivo
salida_archivo = open("amigos_lista.txt", "w")
for i in range(amigos):
    nombre = input("Dime el nombre de tu amigo: ")
    # Escribir en el archivo
    salida_archivo.write(nombre + "\n")

# Cerrar el archivo
salida_archivo.close()

print("Lista de amigos grabada en el archivo")
