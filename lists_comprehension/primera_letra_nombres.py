"""
Dada una lista ["Elie", "Tim", "Matt"], cree una variable llamada answer, que es una
nueva lista que contiene la primera letra de cada nombre en la lista.
Yo usaría una lista de comprensión, aunque también podría recorrerla manualmente.
"""

names = ["Elie", "Tim", "Matt"]
answer = [name[0] for name in names]

print(answer)
