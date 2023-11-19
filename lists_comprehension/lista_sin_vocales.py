"""
Dada la cadena "amazing", crea una variable llamada answer, que es una lista que
contiene todas las letras de "amazing", pero no las vocales (a, e, i, o y u).
La respuesta debería verse así: ['m', 'z', 'n', 'g'].
"""
answer = [letra for letra in "amazing" if letra not in ["a", "e", "i", "o", "u"]]
print(answer)

answer = [letra for letra in "amazing" if letra not in "aeiou"]
print(answer)
