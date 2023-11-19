"""
Utilizando una list comprehension anidada y range(), crea una variable llamada
answer con el siguiente valor:  [[0, 1, 2], [0, 1, 2], [0, 1, 2]].
Para desglosarlo...comienza usando el rango y una lista de compilación para generar la
lista [0,1,2]. Y luego repita todo eso 3 veces en una lista anidada.
Es un poco complicado de discutir, así que tal vez sea mejor buscar la solución
si te quedas atascado.
"""
answer = [[num for num in range(3)] for i in range(3)]
print(answer)
