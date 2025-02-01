# Created by: Ing. José Luis García Morales on 28 de junio de 2020, 11:14
# Este programa utiliza el operador de modulo: %

numero = int(input("Escribe un número: "))

if numero % 4 == 0:
    print(f"{numero} es múltiplo de cuatro y de dos")
elif numero % 2 == 0:
    print(f"{numero} es múltiplo de dos")
else:
    print(f"{numero} no es múltiplo de dos")
