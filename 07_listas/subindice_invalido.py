# subindice_invalido.py
print("-" * 100)
# Este programa usará un subindice no válido en una lista

valores = [0] * 3

print("Intento de guardar 4 números en una lista de 3 elementos.")
for index in range(4):
    valores[index] = 10
    print(f"Procesando el elemento {index}: {valores[index]}")
