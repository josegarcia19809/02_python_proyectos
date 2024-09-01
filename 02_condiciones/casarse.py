print("Consejos que no pediste...")

tienes_casa_propia = input("¿Tienes casa propia (si/no)? ").lower() == "si"
tienes_trabajo_fijo = input("¿Tienes trabajo fijo (si/no)? ").lower() == "si"

if tienes_casa_propia and tienes_trabajo_fijo:
    print("Te puedes casar")
else:
    print("No deberías casarte")
