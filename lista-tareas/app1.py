tareas = []
while True:
    accion_usuario = input("Escribe agregar, mostrar o salir: ")
    accion_usuario = accion_usuario.strip()
    if accion_usuario == "agregar":
        nueva_tarea = input("Ingresa una tarea: ")
        tareas.append(nueva_tarea.capitalize())
    elif accion_usuario == "mostrar":
        for tarea in tareas:
            print(tarea)
    elif accion_usuario == "salir":
        break
    else:
        print("Hey, ingresa una opcion valida")

print("¡Adios!")
