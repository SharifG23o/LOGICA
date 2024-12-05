"""
Programa que recomienda una skin según genero, edad y pavos
Autor: Grupo 1D
Fecha: Marzo 2024
Licencia: GNU GPL V3
"""

from apoyo import ingresar_entero, mostrar_mensaje, ingresar_texto, ingresar_real

def main():
    temporada = ingresar_entero("Ingrese la temporada: ")
    genero = ingresar_texto("Ingrese su género: ")
    edad = ingresar_entero("Ingrese su edad: ")
    pavos = ingresar_real("Ingrese sus pavos en miles: ") * 1000
    mensaje = determinar_mensaje(temporada, genero, edad, pavos)
    mostrar_mensaje(mensaje)

def determinar_mensaje(temporada, genero, edad, pavos):
    
    if temporada < 6:
        mensaje = "Debe tener la temporada 6"
        
    elif genero.lower() != "mujer" and genero.lower() != "hombre":
        mensaje = "Debe tener el género definido"
        
    elif genero.lower() == "mujer" and pavos > 2600 and 18 <= edad <= 25:
        mensaje = "La skin recomendada es Tarana"
        
    elif genero.lower() == "hombre" and pavos > 4900 and 16 <= edad <= 30:
        mensaje = "La skin recomendada es el Caballero Terrible"
        
    elif genero.lower() == "mujer" and pavos <= 2600:
        mensaje = "No tienes suficientes pavos para la skin recomendada"
        
    elif genero.lower() == "hombre" and pavos <= 4900:
        mensaje = "No tienes suficientes pavos para la skin recomendada"

    else:
        mensaje = "No cumple con las condiciones"
    return mensaje


main()