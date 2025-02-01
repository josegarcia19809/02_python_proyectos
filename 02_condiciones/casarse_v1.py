casa_propia = input("¿Tiene casa propia (si/no)? ").lower()
trabajo_fijo = input("¿Tiene trabajo fijo (si/no)? ").lower()

if casa_propia == "si" and trabajo_fijo == "si":
    print("Te puedes casar")
else:
    print("No deberías casarte")
