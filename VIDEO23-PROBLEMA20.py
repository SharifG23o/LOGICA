""""
Programa que permite obtener un mensaje de si el estudiante aprueba o desaprueba un curso
Autor: Programación UQ 
Fecha: Abril 2024 
Liecencia: GNU GPL v3
"""

from apoyo import ingresar_texto, mostrar_mensaje

def main():
    frase = ingresar_texto("Ingrese la frase: ")
   
    mensaje = mensaje_vocales(frase)
    mostrar_mensaje(mensaje)

 

def mensaje_vocales(frase):


    for letra in frase:
    
     if "a" in frase and "e" in frase and "i" in frase and "o" in frase and "u" in frase:
        mensaje = "Tiene todas las vocales"
     else:
        mensaje = "No tiene todas las vocales"
    return mensaje

main()

