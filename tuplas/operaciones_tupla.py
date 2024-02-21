# Creando tuplas
# Para crear una tupla vacía, use paréntesis vacíos:

tupla_estudiante = 'José', 'García', 3.3
print(tupla_estudiante)
print(f"Longitud de la tupla_estudiante: {len(tupla_estudiante)}")

# Empaquetar una tupla separando los valores con comas y usando paréntesis
otra_tupla_estudiante = ('María', 'Rosario', 3.3)
print(otra_tupla_estudiante)

# Si la tupla solo lleva un elemento, debe finalizar la
# lista de elementos con una coma, los parentesis serian opcionales
tupla_un_solo_elemento = ('rojo',)  # notar la coma
print(tupla_un_solo_elemento)

tupla_otro_elemento = 5.5,  # si no se pone la coma contaria como entero y no como tupla
print(tupla_otro_elemento)
