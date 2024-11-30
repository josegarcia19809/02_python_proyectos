total = 0


def incrementar():
    global total
    total += 1
    return total


print(incrementar())
print(incrementar())
print(incrementar())


# El código define una variable global y una función que modifica y devuelve el valor de
# esa variable. Aquí está el desglose:
#
# total = 0: Declara e inicializa una variable global total con el valor 0.
#
# def incrementar():: Define una función llamada incrementar.
#
# Dentro de la función:
#
# global total: Indica que se usará la variable global total dentro de la función,
# en lugar de crear una nueva variable local con el mismo nombre.
# total += 1: Incrementa el valor de total en 1.
# return total: Devuelve el nuevo valor de total.
# print(incrementar()):
#
# Llama a la función incrementar, que incrementa el valor de total a 1
# (inicialmente era 0) y devuelve ese valor.
# La función devuelve 1, que es lo que se imprime.
# Se manda llamar otras 2 veces