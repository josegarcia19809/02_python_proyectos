# Creado por José Luis García. Lunes 19 de agosto de 2024
# Este programa actualiza los pasajeros que suben y bajan de un camión
print("-"*50)
print("Programa que actualiza los pasajeros que suben y bajan de un camión")

pasajeros = 0

# Primera parada: suben 30
pasajeros = pasajeros + 30
print(f"1. Pasajeros: {pasajeros}")

# Segunda parada: bajan 10 y suben 4
pasajeros = pasajeros - 10
pasajeros = pasajeros + 4
print(f"2. Pasajeros: {pasajeros}")

# Tercera parada: bajan 8 y suben 2
pasajeros -= 8
pasajeros += 2
print(f"3. Pasajeros: {pasajeros}")

# Cuarta parada: bajan 1 y suben 2
pasajeros -= 1
pasajeros += 2
print(f"4. Pasajeros: {pasajeros}")

# Quinta parada: bajan 1 y suben 1
pasajeros = pasajeros - 1  # pasajeros--
pasajeros = pasajeros + 1  # pasajeros++
print(f"5. Pasajeros: {pasajeros}")