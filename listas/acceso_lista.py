people = ["Hanna", "Louisa", "Claudia", "Angela", "Geoffrey", "aparna"]

"""
Estoy celebrando una fiesta e hice una lista de las personas que quiero invitar.
Desafortunadamente, soy un amigo terrible y cometí un par de errores de ortografía.
¡Ayúdame a corregirlos! Cambia "Hanna" por "Hannah" (debe haber una 'h' al final)
Cambia "Geoffrey" por "Jeffrey" Cambia "aparna" por "Aparna"(escriba en mayúscula)
Sugerencia: puedes usar la siguiente sintaxis para cambiar un valor de un elemento de 
lista existente en la posición de índice específica: 
lst[0] = "NewValue" 
Aquí, lst representaría la variable que contiene la lista que estamos modificando, 
y el 0 entre corchetes sería el número de índice del elemento objetivo de la lista que 
estamos cambiando, y usaríamos el operador de asignación = para establecerlo 
en un nuevo valor. 
Puedes utilizar este enfoque con la lista de personas de este ejercicio para realizar 
las modificaciones necesarias, como se indicó anteriormente.
"""
print(people)
# Change "Hanna" to "Hannah"
people[0] = people[0] + "h"
# Change "Geoffrey" to "Jeffrey"
people[4] = "Jeffrey"
# Change "aparna" to "Aparna" (capitalize it)
people[5] = people[5].capitalize()

print(people)
