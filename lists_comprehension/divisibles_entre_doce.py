"""
Para todos los números entre 1 y 100 (incluido 100), crea una variable llamada
answer, que contenga una lista con todos los números que son divisibles por 12. (12, 24,
etc.)
"""

answer = [num for num in range(1, 101) if num % 12 == 0]
print(answer)
