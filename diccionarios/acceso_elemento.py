"""
Dado el siguiente diccionario: 
    artist = {
        "first": "Neil",
        "last": "Young",
    }
Declara una variable llamada full_name que es igual al nombre y apellido (first, last)
del artista con un espacio entre ellos. Debes hacer referencia a los valores asociados
con esas claves en el diccionario del artista.
    print(full_name) # Neil Young
"""

artist = {
    "first": "Neil",
    "last": "Young",
}
full_name = f"{artist['first']} {artist['last']}"
print(full_name)  # Neil Young
