""""
Programa para determinar si un aspirante al ejercito es apto o no 
Autor: Area de programacion UQ
Fecha: Febrero 2024
Licencia: GNU GPL v3
"""

from apoyo import ingresar_texto, ingresar_real, ingresar_entero, mostrar_mensaje 

def main():
    genero= ingresar_texto("Ingrese su genero:")
    estado_civil= ingresar_texto("Ingrese su estado civil:")
    estatura= ingresar_real("Ingrese su estatura:")
    edad= ingresar_entero("Ingrese su edad:")
    ingresa_apirante= verificar_ingresa_aspirante(genero, estado_civil,estatura, edad) 
    mensaje_incorporacion= generar_mensaje_incorporacion(ingresa_apirante)
    mostrar_mensaje(mensaje_incorporacion)

def verificar_ingresa_aspirante(genero, estado_civil, estatura,edad):
    ingresa_mujer= verificar_ingresa_mujer(genero, estado_civil,estatura,edad)
    ingresa_hombre= verificar_ingresa_hombre(genero, estado_civil,estatura,edad)
    ingresa_aspirante= ingresa_mujer or ingresa_hombre
    return ingresa_aspirante

def verificar_ingresa_mujer(genero, estado_civil,estatura,edad):
    ingresa_mujer=  genero== "mujer" and estado_civil== "soltera" and estatura >1.60 and edad >= 20 and edad <=25
    return ingresa_mujer

def verificar_ingresa_hombre(genero, estado_civil,estatura,edad):
    ingresa_hombre=  genero== "hombre" and estado_civil== "soltero" and estatura >1.65 and edad >= 18 and edad <=24
    return ingresa_hombre

def generar_mensaje_incorporacion(ingresa_aspirante):
    if ingresa_aspirante:
        mensaje="El aspirante es apto para ser incorporado"

    else: 
        mensaje="El aspirante NO es apto para ser incorporado"
    return mensaje

main()