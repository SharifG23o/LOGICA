"""
Programa que permite crear las tablas de multiplicar
autor: programacion UQ
fecha: abril 2024 
licencia: GNU GPL v3
"""

from apoyo import ingresar_entero_rango, mostrar_mensaje, generar_mensaje_tabla_multiplicar, ingresar_entero_mayor_que

MINIMO_VALOR_TABLA = 0
MAXIMO_VALOR_TABLA = 10
MINIMA_TABLA = 0
MAXIMA_TABLA = 20


def main():

    limite_inferior = ingresar_entero_rango(
        "Ingrese el límite inferior: ", MINIMA_TABLA, MAXIMA_TABLA)
    limite_superior = ingresar_entero_rango(
        "Ingrese el límite superior: ", limite_inferior, MAXIMA_TABLA)
    mensaje_tablas = generar_tablas_de_multiplicacion(
        limite_inferior, limite_superior, MINIMO_VALOR_TABLA, MAXIMO_VALOR_TABLA)
    mostrar_mensaje(mensaje_tablas)


def generar_tablas_de_multiplicacion(limite_inferior, limite_superior, valor_minimo, valor_maximo):
    mensaje_tablas = f"\n TABLAS DE MULTIPLICACION ENTRE {limite_inferior} y {limite_superior}\n"
    i = limite_inferior
    while i <= limite_superior:
        mensaje_tablas += generar_mensaje_tabla_multiplicar(
            i, valor_minimo, valor_maximo)
        i = i+1
    return mensaje_tablas


main()
