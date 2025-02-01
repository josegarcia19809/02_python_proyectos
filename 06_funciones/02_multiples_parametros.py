# 02_multiples_parametros.py
# Este programa define una función "maximo" que determina y devuelve
# el mayor de tres valores: luego se llama a la función tres veces
# 1) con números enteros, 2)números de punto flotante y 3)05_cadenas, respectivamente


def maximo(valor1, valor2, valor3):
    """Retorna el máximo de 3 valores"""
    valor_maximo = valor1
    if valor2 > valor_maximo:
        valor_maximo = valor2
    if valor3 > valor_maximo:
        valor_maximo = valor3
    return valor_maximo


print(f"El máximo es {maximo(12, 27, 36)}")  # evalua el máximo de 3 enteros
print(f"El máximo es {maximo(12.3, 45.6, 9.7)}")  # evalua el máximo de 3 flotantes
print(f"El máximo es {maximo('yellow', 'red', 'orange')}")  # evalua el máximo de 3 05_cadenas
