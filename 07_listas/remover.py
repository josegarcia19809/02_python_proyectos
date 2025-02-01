# remover.py

frutas  = ["manzana", "pera", "mango", "sandía", "melón"]

# Mostrar el índice y el nombre de la fruta
for index, fruta in enumerate(frutas):
    print(f"{index}: {fruta}") 
print()

# Remover un elemento por nombre
frutas.remove("sandía")

for index, fruta in enumerate(frutas):
    print(f"{index}: {fruta}") 
print()

# Remover un elemento por índice
frutas.pop(2)

for index, fruta in enumerate(frutas):
    print(f"{index}: {fruta}") 
print()