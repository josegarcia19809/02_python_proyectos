from typing import List


class Empleado:
    def __init__(self, id_empleado: int, nombre: str, apellido: str):
        self.id: int = id_empleado
        self.nombre: str = nombre
        self.apellido: str = apellido

    def __str__(self) -> str:
        return f"Empleado{{id={self.id}, nombre='{self.nombre}', apellido='{self.apellido}'}}"


def imprimir_lista_empleados(empleados: List[Empleado]) -> None:
    for empleado in empleados:
        print(empleado)
    print("-" * 100)


if __name__ == "__main__":
    print("-" * 100)
    # Crear una lista de Empleados: lista_empleados
    lista_empleados: List[Empleado] = []

    # Agregar 3 elementos a la lista
    lista_empleados.append(Empleado(123, "José", "García"))
    lista_empleados.append(Empleado(345, "Rox", "Sanchéz"))
    lista_empleados.append(Empleado(456, "Fabiola", "Velez"))

    # Imprimir la lista
    imprimir_lista_empleados(lista_empleados)

    # Recuperar el Empleado en la posición 1
    print("Empleado en la posición 1: ")
    print(lista_empleados[1])
    print("-------------------------------")

    # Comprobar si la lista está vacía
    print("¿Está vacía la lista de Empleados?")
    print(len(lista_empleados) == 0)
    print("-------------------------------")

    # Reemplazar un elemento existente
    lista_empleados[1] = Empleado(678, "Arturo", "Morales")

    # Imprimir la lista
    imprimir_lista_empleados(lista_empleados)

    # Añadir un elemento en el índice 1
    lista_empleados.insert(1, Empleado(4567, "Eva", "Luna"))
    imprimir_lista_empleados(lista_empleados)

    # Remover al Empleado del índice 2
    lista_empleados.pop(2)
    imprimir_lista_empleados(lista_empleados)
