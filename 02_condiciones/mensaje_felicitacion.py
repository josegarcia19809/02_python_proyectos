print("-"*100)
print("Este programa saca el promedio de 3 calificaciones")
# Pide las 3 calificaciones
calificacion1 = int(input("Dame calificacion 1: "))
calificacion2 = int(input("Dame calificacion 2: "))
calificacion3 = int(input("Dame calificacion 3: "))
# Calcular el promedio
promedio = (calificacion1 + calificacion2 + calificacion3) / 3
# si el promedio es mayor que 95 mostrar el mensaje "Es un gran promedio"
if promedio > 95:
    print(f"Es un buen promedio")

# Imprime el promedio
print(f"Promedio es {promedio}")
