"""
# Crea una lista de instructores llamada instructors

# Agregue las siguientes cadenas a la lista de instructores
    # "Colt"
    # "Blue"
    # "Lisa"

# Elimina el último valor de la lista.

# Elimina el primer valor de la lista.

# Agrega la cadena "Done" al principio de la lista.

# ¡Ejecuta las pruebas para asegurarse de haberlo hecho correctamente!
"""
instructors = []
instructors.extend(["Colt", "Blue", "Lisa"])
instructors.pop()
instructors.pop(0)
instructors.insert(0, "Done")
print(instructors)
