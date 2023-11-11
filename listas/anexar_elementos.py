"""
Ejercicio de conceptos básicos de listas
Ahora que hemos aprendido sobre las listas, practiquemos un poco.
Ve los enunciados del problema en los comentarios a continuación:

# Crea una lista llamada instructors

# Agregue las siguientes cadenas a la lista de instructores
     # "Colt"
     # "Blue"
     # "lisa"

# ¡Ejecuta las pruebas para asegurarse de haberlo hecho correctamente!
"""

instructors = []
instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")
print(instructors)

# Usando extends
instructors = []
instructors.extend(["Colt", "Blue", "Lisa"])
print(instructors)
