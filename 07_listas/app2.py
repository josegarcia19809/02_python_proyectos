import os
import os.path
os.system("clear") # cls

tareas = []
# Checar si nuestro archivo existe, si existe leemos el contenido, pero si no existe lo creamos
existe_archivo = os.path.exists("tareas.txt")
if existe_archivo:
    # Leer el archivo
    archivo = open("tareas.txt", "r")
    for linea in archivo.readlines():
        linea = linea.strip("\n")
        tareas.append(linea)
    archivo.close()
else:
    # Crearlo
    archivo = open("tareas.txt", "w")
    archivo.close()


while True:
    accion_usuario = input("Escribe agregar, mostrar, editar, quitar o salir: ")
    accion_usuario = accion_usuario.strip().lower()
    
    if accion_usuario == "agregar":
        tarea = input("Ingresa una tarea: ")
        tareas.append(tarea.capitalize())
        
    elif accion_usuario == "mostrar":
        for index, elemento in enumerate(tareas):
            print(f"{index + 1}: {elemento}")
        print()
    
    elif accion_usuario == "editar":
        numero = int (input("Dame número de la tarea a editar: "))
        numero -= 1
        nueva_tarea= input("Dame nuevo nombre de tarea: ")
        tareas[numero] = nueva_tarea.capitalize() 
    
    elif accion_usuario == "quitar":
        numero = int (input("Dame número de la tarea a quitar: "))
        numero -= 1
        tareas.pop(numero)
    
    elif accion_usuario == "salir":
        break
        
    else:
        print("No has ingresado una instrucción válida")

# Escribir todas las tareas en el archivo antes de que finalice
archivo = open("tareas.txt", "w")
for elemento in tareas:
    archivo.write(f"{elemento}\n")
    
archivo.close()
print("Adios")