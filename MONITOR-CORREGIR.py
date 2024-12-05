"""
programa que permite calcular el factorial de un mumero
autor: prog. UQ 
fech: abril 2024
licencia: GNU GPL v3 

"""

from apoyo import ingresar_entero, mostrar_mensaje


def main():
    numero = ingresar_entero("Ingrese el número: ")
    factorial = calcular_factorial(numero)
    mensaje = generar_mensaje_factorial(numero, factorial)
    mostrar_mensaje(mensaje)


def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial


def generar_mensaje_factorial(numero, factorial):
    mensaje = f"El factorial de {numero} es {factorial}"
    return mensaje


main()
