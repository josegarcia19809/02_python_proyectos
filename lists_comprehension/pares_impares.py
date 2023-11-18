numeros = [1, 2, 3, 4, 5, 6]
pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 == 1]

print(pares)
print(impares)

nueva_lista = [num * 2 if num % 2 == 0 else num / 2 for num in numeros]
print(nueva_lista)
