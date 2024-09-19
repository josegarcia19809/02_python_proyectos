# Ese programa muestra la tabla de multiplicar de un número solicitado al usuario

print("Tabla de multiplicar")
numero = int(input("Escribe un número: "))

i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i = i + 1
