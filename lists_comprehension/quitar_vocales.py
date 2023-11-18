enunciado = "This is so much fun"
salida = "".join(letra for letra in enunciado if letra not in "aeiou")
print(salida)  # Ths s s mch fn

print([letra for letra in enunciado if letra not in "aeiou"])
# ['T', 'h', 's', ' ', 's', ' ', 's', ' ', 'm', 'c', 'h', ' ', 'f', 'n']

print("...".join(["hey", "amigo"]))  # hey...amigo
