"""
Programa para leer e imprimir los datos de un empleado
autor: programacion uq
fecha: mayo 2024
licencia: GNU GPL v3
"""

from apoyo import ingresar_texto, ingresar_entero, mostrar_mensaje


def main():
    empleado = ingresar_empleado("INGRESAR LOS DATOS DEL EMPLEADO")
    mensaje = convertir_empleado_mensaje(empleado)
    mostrar_mensaje(mensaje)


def ingresar_empleado(mensaje):
    # el mostrar mensaje solo hace de título, se puede quitar
    mostrar_mensaje(mensaje)
    codigo_empleado = ingresar_texto("Ingrese el código: ")
    nombre = ingresar_texto("Ingrese el nombre del empleado")
    apellido = ingresar_texto("Ingrese los apellidos o apellido: ")
    edad = ingresar_entero("Ingrese la edad: ")
    sueldo = ingresar_entero("Ingrese el sueldo: ")
    empleado = (codigo_empleado, nombre, apellido,
                edad, sueldo)  # esta es la tupla
    return empleado
# retorna todo lo ingresado


def convertir_empleado_mensaje(empleado):
    # acá necesito algo que me permita traer todos los datos al mensaje, osea, sacar las variables
    # empleado, es una tupla, por lo tanto

    codigo_empleado, nombre, apellido, edad, sueldo = empleado  # desempaquetamos la tupla
    # los nombres se pueden cambiar pero no el orden

    mensaje = f"{codigo_empleado}: {nombre}, {apellido}, con edad {edad} años gana {sueldo}\n"
    # también se puede con las posiciones: osea, {empleado[0]}, etc, pero de la otra manera ganamos legibilidad
    #cuando vaya a imprimir, el orden de las variables si no importan


# se hace el f"" y se retorna
    return mensaje


main()
