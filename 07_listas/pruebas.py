# pruebas.py

"""
¿Qué imprime el siguiente código?
"""
no_lista = 4
horas = [20, 24, 30, 18, 2 * no_lista, 40]
# [20, 24, 30, 18, 8, 40]

pago_hora = 100

NUM_EMPLEADOS = len(horas) # 6

for index in range(NUM_EMPLEADOS):
    pago_total = horas[index] * pago_hora
    print(pago_total)

