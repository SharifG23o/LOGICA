"""
Programa que permite infresar una puntuación de o a 100
Autor: programación UQ 
Fecha:Abril 202
Licencia: GNU GPL v3
"""

from apoyo import ingresar_entero_mayor_que, mostrar_mensaje

def main(): 
    puntuacion=ingresar_entero_mayor_que("Ingrese la puntiuación de o a 100: ")
    aprobaion=determinar_aprobacion(puntuacion)
    mostrar_mensaje(aprobaion)

def determinar_aprobacion(puntuacion):
    


    for i in range(0,100):

        if puntuacion >=0 and puntuacion<=50:
            mensaje= "DESAPROBADO"
        elif puntuacion>50 and puntuacion<=75:
            mensaje= "EN BUEN PUNTO"
        else:
            mensaje="APROBADO"
        return mensaje

       
main()

