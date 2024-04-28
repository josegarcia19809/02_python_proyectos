# Implementa una estructura de datos de Pila usando una lista en Python
from typing import List


class Pila(object):

    def __init__(self, maximo: int):  # Constructor
        self.__lista_pila: List[str] = [None] * maximo  # La pila almacenada como una
        # lista de cadenas
        self.__tope: int = -1  # Ningún elemento inicialmente

    def push(self, elemento: str) -> None:  # Insertar elemento en la parte superior de
        # la pila
        self.__tope += 1  # Avanzar el puntero
        self.__lista_pila[self.__tope] = elemento  # Almacenar el elemento

    def pop(self) -> str:  # Quitar el elemento superior de la pila
        elemento_superior: str = self.__lista_pila[self.__tope]  # Elemento superior
        self.__lista_pila[self.__tope] = None  # Quitar referencia al elemento
        self.__tope -= 1  # Decrementar el puntero
        return elemento_superior  # Devolver el elemento superior

    def peek(self) -> str:  # Devolver el elemento superior
        if not self.is_empty():  # Si la pila no está vacía
            return self.__lista_pila[self.__tope]  # Devolver el elemento superior

    def is_empty(self) -> bool:  # Comprobar si la pila está vacía
        return self.__tope < 0

    def is_full(self) -> bool:  # Comprobar si la pila está llena
        return self.__tope >= len(self.__lista_pila) - 1

    def __len__(self) -> int:  # Devolver el número de elementos en la pila
        return self.__tope + 1

    def __str__(self) -> str:  # Convertir la pila a cadena
        salida: str = "["  # Empezar con corchete izquierdo
        for i in range(self.__tope + 1):  # Recorrer los elementos actuales
            if len(salida) > 1:  # Excepto junto al corchete izquierdo,
                salida += ", "  # separar elementos con coma

            salida += str(self.__lista_pila[i])  # Agregar forma de cadena del elemento

        salida += "]"  # Cerrar con corchete derecho
        return salida
