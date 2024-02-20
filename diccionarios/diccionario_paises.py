"""Programa para manipular un diccionario de paises y sus códigos en Internet"""
codigos_de_paises = {'Finlandia': 'fi', 'Sudáfrica': 'za', 'Nepal': 'np'}
print(codigos_de_paises)

# Determinar si un diccionario está vacío
if codigos_de_paises:
    print("codigos_de_paises tiene elementos")
else:
    print("codigos_de_paises está vacío")

codigos_de_paises.clear()

# Determinar si un diccionario está vacío, ahora si lo estará
if codigos_de_paises:
    print("codigos_de_paises tiene elementos")
else:
    print("codigos_de_paises está vacío")
