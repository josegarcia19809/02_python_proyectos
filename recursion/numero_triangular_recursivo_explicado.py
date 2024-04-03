def numero_triangular(n: int) -> int:
    # Imprime los pasos de la ejecución recursiva para calcular
    # el número triangular enésimo
    print(f"Calculando número triangular #{n}")
    if n < 1:  # Caso base
        print("Caso base. Retornando cero")  # Imprime la información de retorno
        return 0

    valor = n + numero_triangular(n - 1)  # No es el caso base, obtiene el valor
    print(f"Retornando valor {valor} para #{n}")  # Imprime la información de retorno
    return valor


print(numero_triangular(5))
