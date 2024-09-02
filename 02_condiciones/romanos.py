# Solicitar al usuario que ingrese un número entre 1 y 10
numero = int(input("Ingresa un número entre 1 y 10: "))

# Verificar si el número está dentro del rango válido
if numero < 1 or numero > 10:
    print("Número fuera del rango. El programa se cerrará.")
    exit()  # Cierra el programa si la entrada no es válida

# Mostrar la versión en números romanos utilizando sentencias if
if numero == 1:
    print("El número en romano es I")
elif numero == 2:
    print("El número en romano es II")
elif numero == 3:
    print("El número en romano es III")
elif numero == 4:
    print("El número en romano es IV")
elif numero == 5:
    print("El número en romano es V")
elif numero == 6:
    print("El número en romano es VI")
elif numero == 7:
    print("El número en romano es VII")
elif numero == 8:
    print("El número en romano es VIII")
elif numero == 9:
    print("El número en romano es IX")
elif numero == 10:
    print("El número en romano es X")