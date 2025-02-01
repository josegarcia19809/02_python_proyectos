# par_impar.py
import os

os.system("clear")
# Created by: Ing. José Luis García Morales on 28 de junio de 2020, 11:14
# Este programa utiliza el operador de negación: not
# y el operador diferente: !=

numero = int(input("Escribe un número: "))
if numero % 2 != 0:
    print(f"El número {numero} es impar")
else:
    print(f"El número {numero} es par")

# Usando una negación
if not numero % 2:
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
