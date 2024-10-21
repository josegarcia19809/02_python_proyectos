# frutas.py

frutas = []  # Se crea una lista vacía

# Pedir 5 frutas y que las vaya anexando a la lista y después se imprime la lista
for i in range(5):
    nueva_fruta = input("Dame nombre de fruta: ")
    frutas.append(nueva_fruta)

print(frutas)

# Imprimir una fruta por renglón
print()
for fruta in frutas:
    print(fruta)

# Pedir un índice para cambiar la fruta que esté en esa posición.
# Imprimir un mensaje de error si el índice está fuera del rango.

indice = int(input("Dame índice de la fruta a cambiar: "))
if 0 <= indice <= 4:
    nueva_fruta = input("Dame nuevo nombre de fruta: ")
    frutas[indice] = nueva_fruta
    print(frutas)
else:
    print("El índice no es válido")
