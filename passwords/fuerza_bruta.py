import itertools
import string
import time
from typing import Optional


def buscar_palabras_comunes(palabra_a_buscar) -> Optional[str]:
    """Comprueba un archivo lleno de palabras comunes."""

    with open('10-million-password-list-top-100000.txt', 'r') as palabras:
        lista_palabras = palabras.read().splitlines()

    for i, elemento in enumerate(lista_palabras, start=1):
        if elemento == palabra_a_buscar:
            return f'Palabra común: {elemento} (#{i})'


# Pasa por cada combinación de caracteres.
def aplicar_fuerza_bruta(palabra, longitud, digitos=False, simbolos=False) -> Optional[
    str]:
    """Realiza fuerza bruta al encontrar una palabra."""

    # Modifique esto para símbolos totales.
    combinacion = string.ascii_lowercase

    if digitos:
        combinacion += string.digits

    if simbolos:
        combinacion += string.punctuation

    intentos = 0
    for buscar in itertools.product(combinacion, repeat=longitud):
        intentos += 1
        buscar = ''.join(buscar)

        if buscar == palabra:
            return f'"{palabra}" fue hackeada en {intentos:,} intentos.'
        # print(buscar, intentos) # Comenta esto cuando no estés probando


def main():
    print('Buscando...')
    password = 'amor'

    # Obtener la hora de inicio
    tiempo_inicial = time.perf_counter()

    # Busque palabras comunes antes de usar la fuerza bruta real.
    if palabra_comun := buscar_palabras_comunes(password):
        print(palabra_comun)
    else:
        if cracked := aplicar_fuerza_bruta(password, longitud=5, digitos=True,
                                           simbolos=False):
            print(cracked)
        else:
            print('No hubo coincidencias...')

    # Obtener la hora de finalización
    tiempo_final = time.perf_counter()

    # Mostrar el tiempo que tomó
    print(round(tiempo_final - tiempo_inicial, 2), 's')


if __name__ == '__main__':
    main()
