# Inasistencia por enfermedad
# En este ejercicio, se te darán algunas variables que se establecerán aleatoriamente en
# valores booleanos (Verdadero o Falso):
#
# realmente_enfermo - ¡cuando tienes gripe de verdad!
# un_poco_enfermo - te sientes mal y es suficiente con darte un día libre si tienes tiempo
# odias_tu_trabajo - el trabajo apesta, lo sé ...
# También se le asigna un número aleatorio a dias_libres_por_enfermedad entre 0 y 10.
#
# Finalmente, hay una variable llamada inasistencia_por_enfermedad que debe establecer
# en Verdadero o Falso basado en los siguientes escenarios:
#
# Establecer en Verdadero si:
#
# estás realmente enfermo y te quedan días por enfermedad
# estás un poco enfermo y odias tu trabajo y te quedan días libres por enfermedad
# De lo contrario, establézcalo en Falso.
#
# Las pruebas verifican que el valor de inasistencia_por_enfermedad sea correcto
# según las condiciones especificadas anteriormente.

# NO TOCAR ======================================

from random import choice, randint

# asigna aleatoriamente valores a estas cuatro variables
realmente_enfermo = choice([True, False])
un_poco_enfermo = choice([True, False])
odias_tu_trabajo = choice([True, False])
dias_libres_por_enfermedad = randint(0, 10)
print(realmente_enfermo, un_poco_enfermo, odias_tu_trabajo, dias_libres_por_enfermedad)
# NO TOUCHING ======================================
# Establece esta variable en True o False con lógica boleana y condicionales!
inasistencia_por_enfermedad = None

# Tu código empieza aquí vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv


# Tu código acaba aquí  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
print(inasistencia_por_enfermedad)
