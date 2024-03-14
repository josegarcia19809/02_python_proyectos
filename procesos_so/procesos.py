procesos = []
while True:
    accion_usuario = input("Escribe agregar, mostrar o salir: ")
    accion_usuario = accion_usuario.strip()
    if accion_usuario == "agregar":
        nuevo_proceso = input("Ingresa un proceso: ")
        procesos.append(nuevo_proceso.capitalize())
    elif accion_usuario == "mostrar":
        for proceso in procesos:
            print(proceso)
    elif accion_usuario == "salir":
        break
    else:
        print("Hey, has ingresado una instrucción desconocida")

print("Adios")
