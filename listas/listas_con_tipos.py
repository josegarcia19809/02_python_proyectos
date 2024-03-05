# listas_con_tipos.py
from typing import List

N: int = 8  # tamaño de la lista
x: List[float] = [14.0, 12.0, 8.0, 7.0, 6.41, 5.23, 6.15, 7.25]
# Imprimir la lista
print("Lista x: ", end="")
for i in range(0, N):
    print(f"{x[i]}", end=" ")
print()

# Imprimir el elemento [1]
print(f"x[1]: {x[1]}")

# Cambiar el elemento [4] a 45 e imprimir la lista
x[4] = 45
print("Lista x: ", end="")
for i in range(0, N):
    print(f"{x[i]}", end=" ")
print()

# Declarar una variable suma sumar los elementos [1] y [3]
suma: float = x[1] + x[3]
print(f"suma: {suma}")

# Añadir a suma lo que tenga el elemento [4]
suma = suma + x[4]
print(f"suma: {suma}")

# Añadir al elemento [5] 3.5 unidades (5.23 + 3.5 -> 8.73) e imprimir la lista
x[5] = x[5] + 3.5
print("Lista x: ", end="")
for i in range(0, N):
    print(f"{x[i]}", end=" ")
print()

# Modificar el elemento [6], que sea la suma de los elementos [1] y [2]
# (x[6] --> 12.0 + 8.0 --> 20) e imprimir la lista
x[6] = x[1] + x[2]

print("Lista x: ", end="")
for i in range(0, N):
    print(f"{x[i]}", end=" ")
print()

print(f"La longitud de la lista: {len(x)}")
