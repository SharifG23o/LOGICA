"""
Programa que impime la sucesión de finonacci 
Autor:Programación UQ 
Fecha:Abril 2024
Licencia: GNU GPL v3

"""

from apoyo import ingresar_entero_mayor_que, mostrar_mensaje

MINIMO_VALOR = 0


def main():
    limite_inferior = ingresar_entero_mayor_que(
        "Ingrese el límite inferior: ", MINIMO_VALOR)
    limite_superior = ingresar_entero_mayor_que(
        "Ingresar límite superior: ", limite_inferior)
    cantidad_fibonacci = contar_terminos_fibonacci(
        limite_inferior, limite_superior)
    mensaje_fibonacci = generar_mensaje_fibonacci(
        limite_inferior, limite_superior, cantidad_fibonacci)
    mostrar_mensaje(mensaje_fibonacci)


def contar_terminos_fibonacci(limite_inferior, limite_superior):
    cantidad_termino = 0
    a = 1
    b = 1
    while a <= limite_superior:
        if a >= limite_inferior:
            cantidad_termino = cantidad_termino+1
            c = a+b
            a = b
            b = c
    return cantidad_termino


def generar_mensaje_fibonacci(limite_inferior, limite_superior, cantidad_fibonacci):
    mensaje = f" Entre {limite_inferior} y {limite_superior} hay {
        cantidad_fibonacci} términos de la sucesión de Fibonacci"
    return mensaje


main()
