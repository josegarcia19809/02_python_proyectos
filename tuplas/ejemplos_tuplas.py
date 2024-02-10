tup = 1, 2, 3
a, b, c = tup

print(a * b * c)  # 6

# Completa el código para emplear correctamente el método count() para encontrar la
# cantidad de 2 duplicados en la tupla siguiente.

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)  # salida: 4

# Escribe un programa que convierta la lista my_list en una tupla.
my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list)
print(t)

# Escribe un programa que convierta la tupla colors en un diccionario.

colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)

print(colors_dictionary)

# ¿Que ocurrirá cuando se ejecute el siguiente código?

my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()

print(copy_my_dictionary)  # {'A': 1, 'B': 2}

# ¿Cuál es la salida del siguiente programa?

colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
}

for col, rgb in colors.items():
    print(col, ":", rgb)

"""
blanco : (255, 255, 255)
gris : (128, 128, 128)
rojo : (255, 0, 0)
verde : (0, 128, 0)
"""
