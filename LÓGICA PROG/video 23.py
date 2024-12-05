""""
Programa que permite obtener un mensaje de si el estudiante aprueba o desaprueba un curso
Autor: Programación UQ 
Fecha: Abril 2024 
Liecencia: GNU GPL v3
"""

from apoyo import mostrar_mensaje,ingresar_real

NOTA_APROBACION=3.0

def main(): 
    nota_definitiva=ingresar_real("Ingrese su nota definitiva: ")
    mensaje=generar_mensaje_nota(nota_definitiva)
    mostrar_mensaje(mensaje)

def generar_mensaje_nota(nota_definitiva):

    if NOTA_APROBACION>=3.0:
        mensaje= f"Con una nota definitiva de {nota_definitiva}, usted aprueba el curso"
    else:
        mensaje=f"Con una nota definitiva de {nota_definitiva}, usted no aprueba el curso"

main()

