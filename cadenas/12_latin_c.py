def EscribirPalabraEnLatin(pal):
    i = 1
    while i <= len(pal) - 1:
        print(pal[i], end="")
        i += 1
    print(f"{pal[0]}ae")


frase = input("Escriba una frase: ")

palabra = ""

for i in range(0, len(frase)):
    if frase[i] != " ":
        palabra += frase[i]
    else:
        EscribirPalabraEnLatin(palabra)
        palabra = ""

EscribirPalabraEnLatin(palabra)
print("-"*100)