"""
Programa que imprime una figura según un número n
Autor: programación uq 
Fecha: abril 2024
Licencia: GNU GPL v3
"""


from apoyo import ingresar_entero_mayor_que, mostrar_mensaje


MINIMO_VALOR=0

def main():
    numero= ingresar_entero_mayor_que("Ingrese el valor n: ", MINIMO_VALOR)
    figura= gener