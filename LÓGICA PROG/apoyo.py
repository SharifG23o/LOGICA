""""
Modulo de funciones
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""


def ingresar_texto(mensaje):
    texto= input(mensaje)
    return texto


def ingresar_entero(mensaje):
    valor= int(input(mensaje))
    return valor


def ingresar_real(mensaje):
    valor= float(input(mensaje))
    return valor

def mostrar_mensaje(mensaje):
    print(mensaje)


def calcular_promedio( valor1, valor2, valor3, valor4, valor5):
    promedio=(valor1 + valor2 + valor3 + valor4+ valor5) / 5
    return promedio



 