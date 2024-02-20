diccionario_pilotos = {'Piloto 1': 'Fernando', 'Piloto 2': 'Rosario',
                       'Piloto 3': 'Luis'}
print(diccionario_pilotos)

# get(): Devuelve el valor que corresponde con la key introducida.

print(diccionario_pilotos.get('Piloto 1'))
print("Obtener valor de key 'Piloto 1': ", end="")
# pop(): Devuelve el valor que corresponde con la key introducida, 
# y luego borra la key y el valor.
print("Borrando Piloto 1: ", end="")
print(diccionario_pilotos.pop('Piloto 1'))
print(diccionario_pilotos)

# update(): Actualiza el valor de una determinada key o lo crea si no existe.
diccionario_pilotos.update({'Piloto 4': 'Lewis Hamilton'})
diccionario_pilotos.update({'Piloto 2': 'César'})
print(diccionario_pilotos)

# "key" in diccionario_pilotos: devuelve verdadero (True) o falso (False) si la key existe 
# en el diccionario_pilotos.
print("Existe key 'Piloto 1' en diccionario_pilotos?: ", end="")
print("Piloto 1" in diccionario_pilotos)
print("Existe key 'Piloto 2' en diccionario_pilotos?: ", end="")
print("Piloto 2" in diccionario_pilotos)
print("Existe key 'César' en diccionario_pilotos?: ", end="")
print("César" in diccionario_pilotos)

# "definición" in diccionario_pilotos.values(): devuelve verdadero (True) o falso
# (False) si la definición existe en el diccionario_pilotos.
print("Existe valor 'César' en diccionario_pilotos?: ", end="")
print("César" in diccionario_pilotos.values())

# del diccionario_pilotos['key']: Elimina el valor (y el key) asociado a la key indicada.
print("Eliminando diccionario_pilotos['Piloto 2']", end="")
del diccionario_pilotos['Piloto 2']
print(diccionario_pilotos)
