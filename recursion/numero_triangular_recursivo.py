def numero_triangular(n: int) -> int:
    # Obtener el número triangular enésimo de forma recursiva
    if n < 1:
        return 0  # Para cualquier número menor que 1, es 0
    return (n +  # De lo contrario, añadir esta columna a la anterior
            numero_triangular(n - 1))  # número triangular


print(numero_triangular(100))
print(numero_triangular(200))
print(numero_triangular(500))
