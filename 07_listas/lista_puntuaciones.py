# Incrementos en los elementos de una lista
print("-" * 100)
puntuaciones = [7, 8, 9, 10, 11]
print("Lista original:")
print(puntuaciones)

puntuaciones[2] = puntuaciones[2] + 1  # incremento en 1 del elemento 2 de la lista
puntuaciones[4] += 1  # incremento en 1 del elemento 4 de la lista

print("Después de los incrementos: ")
print(puntuaciones)
