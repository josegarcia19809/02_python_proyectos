# lista_temperaturas
print("-" * 100)

temperaturas = [0.0] * 4

temperaturas[0] = 3.4
temperaturas[1] = 5.8
temperaturas[2] = 20.0
temperaturas[3] = 40.0

longitud_lista = len(temperaturas)
print(f"Tamaño de la lista: {longitud_lista}")
print()

for i in range(len(temperaturas)):
    print(f"Temperatura[{i}]: {temperaturas[i]}")
