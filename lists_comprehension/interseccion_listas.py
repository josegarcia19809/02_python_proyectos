"""
1. Dadas dos listas [1,2,3,4] y [3,4,5,6], crea una variable llamada answer, que es una
nueva lista que es la intersección de las dos. Su resultado debería ser [3,4] .
Sugerencia: utilice el operador in para comprobar si un elemento está en una lista.
Por ejemplo:  5 in [1,5,2]  es Verdadero. 3 in [1,5,2] es falso.
"""
lista_a = [1, 2, 3, 4]
lista_b = [3, 4, 5, 6]
answer = [num for num in lista_a if num in lista_b]
print(answer)

