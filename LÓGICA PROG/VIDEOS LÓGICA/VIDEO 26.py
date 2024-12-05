"""
Programa que permite crear las tablas de multiplicar
autor: programacion UQ
fecha: abril 2024 
licencia: GNU GPL v3
"""

from apoyo import ingresar_entero_rango, mostrar_mensaje, generar_mensaje_tabla_multiplicar2

MINIMO_VALOR_TABLA = 0
MAXIMO_VALOR_TABLA = 10
MINIMA_TABLA = 0
MAXIMA_TABLA = 20


def main():
    
    numero_tabla = ingresar_entero_rango(
        "Ingrese la tabla a generar: ", MINIMA_TABLA, MAXIMA_TABLA)
    mensaje_tabla = generar_mensaje_tabla_multiplicar2(
        numero_tabla, MINIMO_VALOR_TABLA, MAXIMO_VALOR_TABLA)
    mostrar_mensaje(mensaje_tabla)



main()
