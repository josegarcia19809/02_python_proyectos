# Pedir al usuario el número de amigos
amigos = int(input("¿Cuántos amigos tienes? "))

# Abrir el archivo
with open("amigos_lista.txt", "w") as salida_archivo:
    for i in range(amigos):
        nombre = input("Dime el nombre de tu amigo: ")
        # Escribir en el archivo
        salida_archivo.write(nombre + "\n")

print("Lista de amigos grabada en el archivo")
