tareas = ["Barrer", "Trapear", "Planchar"]

while True:
    accion_usuario = input("Escribe agregar, mostrar, editar, quitar o salir: ")
    accion_usuario = accion_usuario.strip()

    if accion_usuario == "agregar":
        tarea = input("Ingresa una tarea: ")
        tareas.append(tarea.capitalize())

    elif accion_usuario == "mostrar":
        for index, elemento in enumerate(tareas):
            print(f"{index + 1}: {elemento}")

    elif accion_usuario == "editar":
        numero = int(input("Dame número de tarea a cambiar: "))
        numero = numero - 1
        nueva_tarea = input("Dame nueva tarea: ")
        tareas[numero] = nueva_tarea.capitalize()

    elif accion_usuario == "quitar":
        numero = int(input("Dame número de tarea a eliminar: "))
        numero = numero - 1
        tareas.pop(numero)

    elif accion_usuario == "salir":
        break

    else:
        print("Hey, has ingresado una instrucción desconocida")

print("¡Adios!")

