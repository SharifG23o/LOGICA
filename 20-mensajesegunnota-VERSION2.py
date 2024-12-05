"""
Programa que permite obtener un mensaje de si el estudiante aprueba o desaprueba un curso
Autor: Programación UQ
Fecha: Abril 2024
Licencia: GNU GPL v3
"""
from apoyo import ingresar_real_rango, mostrar_mensaje

NOTA_MINIMA = 0.0
NOTA_MAXIMA = 5.0
NOTA_MINIMA_GANAR = 3.0


def main():
    nota_final = ingresar_real_rango("Ingrese la nota final: ", NOTA_MINIMA, NOTA_MAXIMA)
    mensaje_nota = generar_mensaje_nota_final(nota_final)
    mostrar_mensaje(mensaje_nota)


def generar_mensaje_nota_final(nota_final):
    if nota_final >= NOTA_MINIMA_GANAR:
        mensaje = "Aprobó el curso"
    else:
        mensaje = "Reprobó el curso"
    return mensaje


main()