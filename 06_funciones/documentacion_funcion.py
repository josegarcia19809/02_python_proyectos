def exponent(num, power=2):
    """exponent(num, power=2) raises num to specified power. Power defaults to 2."""
    return num ** power


print(exponent(2, 3))
print(exponent(3))
print(exponent(7))

print(exponent.__doc__)  # Imprime la documentación de la función
