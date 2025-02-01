# Ejercicio de clasificación de alimentos
# He escrito un código en la parte superior del archivo para usted.
# Por favor, no lo toque, si desea que las pruebas funcionen
# lo que hace el código es establecer aleatoriamente la variable de
# alimentos en 'manzana', 'uva', 'tocino', 'filete', 'gusano' o 'suciedad'.
# No se preocupe por cómo funciona por ahora, aprenderemos más en breve.
# #
# Cuando ejecuta el código preescrito, la comida se asignará al azar.
# Su tarea es escribir un código que clasifique qué es la comida.
# #
# Si la comida está configurada como 'manzana' o 'uva', su código debe imprimir 'fruta'.
# Si la comida está configurada como 'tocino' o 'filete', su código debe imprimir 'carne'
# Si la comida está configurada como 'suciedad' o 'gusano', su código debe imprimir 'yuck'

# NO TOUCHING ============================================
from random import choice

comida = choice(['manzana', 'uva', 'tocino', 'filete', 'gusano', 'suciedad'])
print(f'comida: {comida}')
# NO TOUCHING =============================================

# Aqui va tu código
if comida == 'manzana' or comida == 'uva':
    print('fruta')
elif comida == 'tocino' or comida == 'filete':
    print('carne')
elif comida == 'suciedad' or comida == 'gusano':
    print('yuck')
