from pila_simple import Pila

pila: Pila = Pila(12)
for palabra in ["La", "vida", "es", "lo", "que", "pasa", "mientras", "estamos",
                "ocupados", "haciendo", "otros", "planes"]:
    pila.push(palabra)
    print(len(pila), ":", palabra, end=" ")
    print('¿La pila está llena?', pila.is_full())

if not pila.is_full():
    pila.push("Frase")
else:
    print("No se puede insertar, la pila está llena")


print('Después de agregar', len(pila), 'palabras a la pila, contiene:\n', pila)

print('Sacando elementos de la pila:')
while not pila.is_empty():
    print(pila.pop(), end=' ')
print()
