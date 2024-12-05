"""
Programa que permite observar la secuencia generada por la cojetura de ULAM 
autor:programacion UQ 
fecha:abril 2024
licencia: GNU GPL v3 

"""
from apoyo import ingresar_entero_mayor_que, mostrar_mensaje

VALOR_MINIMO = 1  


def main():
    numero = ingresar_entero_mayor_que("Ingrese el entero: ", VALOR_MINIMO)
    secuencia = obtener_secuencia_ULAM(numero)
    mensaje = genrar_mensaje_secuencia(numero, secuencia)
    mostrar_mensaje(mensaje)


def obtener_secuencia_ULAM(numero):
    secuencia = f"{numero} "
    while numero != 1:
        if numero % 2 == 0:
            numero = numero//2
        else:
            numero = numero*3+1
        secuencia += f"{numero} "
    return secuencia


def genrar_mensaje_secuencia(numero, secuencia):

    mensaje = f" Con el numero siendo {numero} la secuencia es {secuencia}"
    return mensaje


main()
