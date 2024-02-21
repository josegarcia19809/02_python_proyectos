# Programa para crear un comjunto de cadenas que se llame colores
colores = {'rojo', 'naranja', 'amarillo', 'verde', 'rojo', 'azul'}
print(colores)  # Aunque hay 2 'rojo' solo imprime uno

print(f"Número de elementos de colores: {len(colores)}")

# Revisando si existe un determinado elemento en el conjunto
print(f'¿Existe rojo en colores? {"red" in colores}')
print(f'¿Existe morado en colores? {"morado" in colores}')
print(f'¿No existe morado en colores? {"morado" not in colores}')

# Recorrindo el conjunto de colores
for color in colores:
    print(color.upper(), end=' ')  # y convierte las cadenas en mayúsculas

print()
# Crear un conjunto vacio
conjunto_vacio = set()
print(conjunto_vacio)
# Crear un conjunto mediante la unión de 2 listas, se eliminan los duplicados
numeros = list(range(10)) + list(
    range(5))  # se crea primero una lista por medio de sumar 2
print(numeros)
conjunto_numeros = set(numeros)  # Se transforma la lista a un conjunto
print(conjunto_numeros)
