# alumno_en_escuela.py
# import os
#
# os.system("clear")


# Ese programa preguntará a un alumno su calificación (0.0 a 10.0),
# también pedirá su porcentaje de asistencias. El programa tendrá dos funciones:
# esta_aprobado(): mostrará un mensaje de que está aprobado
# no_esta_aprobado(): mostrará un mensaje de que no está aprobado
# Condición para que esté aprobado: 6.0 o más de calificación y que tenga por lo
# menos 80% de asistencias

def esta_aprobado():
    print("Felicidades 😄, ya aprobaste")


def no_esta_aprobado():
    print("Ni modo 😥, no aprobaste")


def main():
    print("Sistema de calificaciones")
    calificacion = float(input("Dame tu calificación: "))
    porcentaje_asistencias = int(input("Dame tu porcentaje de asistencias: "))

    # Verificar si está aprobado
    if calificacion >= 6.0 and porcentaje_asistencias >= 80:
        esta_aprobado()
    else:
        no_esta_aprobado()


main()
