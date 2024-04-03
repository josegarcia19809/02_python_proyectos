def figura_asteriscos(n, total):
    if n == 0:  # Caso base: cuando n llega a 0, termina la recursión
        return
    print(" " * (
            total - n) + "* " * n)  # Imprime la línea con los espacios y los asteriscos
    figura_asteriscos(n - 1,
                      total)  # Llama recursivamente a la función con n-1 y el mismo total


# Función principal para generar la figura de asteriscos
def generar_figura(total):
    figura_asteriscos(total // 2 + 1,
                      total)  # Llama a la función figura_asteriscos con n = total // 2 + 1
    figura_asteriscos(total // 2,
                      total)  # Llama a la función figura_asteriscos con n = total // 2


# Ejemplo de uso
generar_figura(7)
