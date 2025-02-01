# Este programa calcula el total de una serie de calificaciones 
# que un usuario introduce. El usuario introduce la serie de 
# calificaciones hasta que introduce un valor mayor que 100

CALIFICACION_ALTA = 100

calificacion = 0
total = 0
numero_calificacion = 1

print("Programa para calcular el total de calificaciones introducidas.")
print("Introduzca una calificacion entre 0 y 100")
print("Para dejar de introducir calificaciones, introduzca " +
      "cualquier calificacion mayor que 100")

while calificacion <= CALIFICACION_ALTA:
    total = total + calificacion
    calificacion = int(input(f"Introduce la calificacion {numero_calificacion}: "))
    numero_calificacion = numero_calificacion + 1

print(f"La suma total de las calificaciones es {total}")
