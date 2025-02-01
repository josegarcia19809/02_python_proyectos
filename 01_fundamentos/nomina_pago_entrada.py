# Programa que calcula el pago total de un trabajador
# dependiendo cuántas horas trabajo
# y cuánto le pagan por hora

horas_trabajadas = int(input("¿Cuántas horas trabajaste?: "))
pago_por_hora = float(input("¿Cuánto te pagan por hora?: "))
pago_total = horas_trabajadas * pago_por_hora
print(f"Tu pago total es de ${pago_total}")