"""
Programa que permite hacer la sucesión de Fibonacci
autor: programacion UQ
fecha: abril 2024 
licencia: GNU GPL v3
"""

from apoyo import ingresar_entero, mostrar_mensaje

def main():
    numero_serie = ingresar_entero("Ingrese el número de términos de la serie de Fibonacci que desea calcular: ")
    serie = generar_serie(numero_serie)
    mostrar_mensaje(serie)

def generar_serie(numero_serie):
   
main()

    


