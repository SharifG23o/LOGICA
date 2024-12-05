"""
Programa que permite calcular el MCD para 2 numeros 

Autor: Programación UQ
Fecha: Abril 2024
Licencia: GNU GPL v3 

"""

from apoyo import ingresar_entero, mostrar_mensaje


def main():
    a= ingresar_entero("Ingrese el primer número: ")
    b= ingresar_entero("Ingrese el segundo número: ")
    hallar_mcd=calcular_mcd(a,b)
    mostrar_mensaje(hallar_mcd)

def calcular_mcd(a,b): 

    while b != 0:
        a, b = b, a % b
    return a


main()



