import os

os.system("clear")

for num in range(5):  # [0, 1, 2, 3, 4]
    print(num)

print()
print("-" * 50)
# Imprimir 5 veces el mensaje "Hello world"
for x in range(5):
    print("Hello world")


print("-" * 50)

for num in range(1, 5):
    print(num)
    
print("-" * 50)

for num in range(1, 10, 2):
    print(num, end=" ")
    
# Imprimir del 0 al 9
print("-" * 50)

for num in range(10):
    print(num, end=" ")
    
# Imprimir del 10 al 20
print("-" * 50)

for num in range(10, 21):
    print(num, end=" ")
    
# Imprimir del 9 al 1 en forma descendente
print("-" * 50)

for num in range(9, 0, -1):
    print(num, end=" ")
    
# Mostrar el mensaje "Debo hacer mi tarea"
# 100 veces
print("-" * 50)

for num in range(100):
    print("Debo hacer mi tarea")