"""
2. Dada una lista de palabras ["Elie", "Tim", "Matt"] crea una variable llamada answer2,
que es una nueva lista con cada palabra invertida y en minúsculas (¡usa un slice
para hacer la inversión!) Tu la salida debe ser ['eile', 'mit', 'ttam']
"""

palabras = ["Elie", "Tim", "Matt"]
answer2 = [palabra.lower()[::-1] for palabra in palabras]
print(answer2)
