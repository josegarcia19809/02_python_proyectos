import os.path

tareas = []
nombre_archivo = "tareas.txt"


def crear_archivo():
    existe_archivo = os.path.exists(nombre_archivo)
    if not existe_archivo:
        # Crearlo
        archivo = open(nombre_archivo, "w")
        archivo.close()


def leer_archivo():
    existe_archivo = os.path.exists(nombre_archivo)
    if existe_archivo:
        # Abrir el archivo
        archivo = open(nombre_archivo, "r")
        # Leer el archivo
        for linea in archivo.readlines():
            linea = linea.strip("\n")
            tareas.append(linea)
        archivo.close()


def escribir_en_archivo():
    archivo = open(nombre_archivo, "w")
    for elemento in tareas:
        archivo.write(f"{elemento}\n")

    archivo.close()


def agregar_tarea():
    tarea = input("Ingresa una tarea: ")
    tareas.append(tarea.capitalize())
    escribir_en_archivo()


def mostrar_tareas():
    for index, elemento in enumerate(tareas):
        print(f"{index + 1}: {elemento}")


def editar_tarea():
    mostrar_tareas()
    try:
        numero = int(input("Dame número de tarea a cambiar: "))
        numero = numero - 1
        nueva_tarea = input("Dame nueva tarea: ")
        tareas[numero] = nueva_tarea.capitalize()
        escribir_en_archivo()
    except IndexError:
        print("**********Indice fuera de rango")


def quitar_tarea():
    mostrar_tareas()
    try:
        numero = int(input("Dame número de tarea a eliminar: "))
        numero = numero - 1
        tareas.pop(numero)
        escribir_en_archivo()
    except IndexError:
        print("**********Indice fuera de rango")


def main():
    crear_archivo()
    leer_archivo()
    while True:
        accion_usuario = input("Escribe agregar, mostrar, editar, quitar o salir: ")
        accion_usuario = accion_usuario.strip()

        if accion_usuario == "agregar":
            agregar_tarea()

        elif accion_usuario == "mostrar":
            mostrar_tareas()

        elif accion_usuario == "editar":
            editar_tarea()

        elif accion_usuario == "quitar":
            quitar_tarea()

        elif accion_usuario == "salir":
            break

        else:
            print("Hey, has ingresado una instrucción desconocida")

    print("¡Adios!")


if __name__ == '__main__':
    main()
