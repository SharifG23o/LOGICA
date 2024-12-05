"""
Programa para determinar cuantas cajas completas de fruta fresca se necesitan para trasladar un pedido
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""

CAPACIDAD_MAXIMA=25

def main():
    cantidad_libros= ingresar_entero("ingrese la cantidad de libros: ")
    cantidad_estanterias= calcular_cantidad_estanterias(cantidad_libros, CAPACIDAD_MAXIMA)
    espacio_extra= calcular_espacio_extra(cantidad_libros, CAPACIDAD_MAXIMA)
    mensaje= generar_mensaje(cantidad_estanterias, espacio_extra)

def ingresar_entero(mensaje):
    entero= int(input(mensaje))
    return entero

def calcular_cantidad_estanterias(cantidad_libros,CAPACIDAD_MAXIMA):
    cantidad_estanterias= cantidad_libros//CAPACIDAD_MAXIMA
    return cantidad_estanterias


def calcular_espacio_extra(cantidad_libros, capacidad_maxima):
    espacio_extra= cantidad_libros%capacidad_maxima
    return espacio_extra

def generar_mensaje(cantidad_estanterias, espacio_extra):

    if espacio_extra==0:
         mensaje= f"se necesitan {cantidad_estanterias} estanterias y se necesita espacio para {espacio_extra}libros"

    else:
        mensaje= f"se necesitan {cantidad_estanterias} estanterias"

    return mensaje

def mostrar_mensaje(mensaje):
    print(mensaje)



main()
