# presenta_ordinario.py
import os

os.system("clear")


# Definir una función que reciba el número de clases que hubo en el semestre y el número de asistencias de un alumno. La función debe devolver True si el alumno tiene por lo menos 80% de asistencias para presentar ordinario. Devolverá False en caso contrario

def puede_presentar_examen(num_clases: int, num_asistencias: int) -> bool:
    porcentaje_asistencias = num_asistencias * 100 / num_clases
    if porcentaje_asistencias >= 80:
        return True
    else:
        return False


def main():
    numero_clases = int(input("¿Cuántas clase hubo? "))
    asistencias = int(input("¿Cuántas asistencias tuvo el alumno? "))

    if puede_presentar_examen(numero_clases, asistencias):
        print("Puede presentar examen ordinario")
    else:
        print("NO puede presentar examen ordinario")


main()
