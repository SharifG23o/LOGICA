""""
Programa para determinar el mensaje en una persecucion policiaca 
Autor: Area de programacion UQ
Fecha: Marzo 2024
Licencia: GNU GPL v3
"""


from apoyo import ingresar_real, mostrar_mensaje 

LIMITE1= 0.0
LIMITE2= 0.75 #45 MN/60
LIMITE3= 1.50
LIMITE4=2.00
TIEMPO_INDETERMINADO=-1

def main():
    velocidad_infractor=ingresar_real("Ingrese la velocidad del infractor en Km/h: ")
    tiempo_infraccion= ingresar_real("Ingrese el tiempo de la infraccion en horas: ")
    velocidad_policia= ingresar_real("Ingrese la velocidad del policia en Km/h: ")
    tiempo_intercepcion=calcular_tiempo_intercepcion(velocidad_infractor, velocidad_policia,tiempo_infraccion)
    mensaje_policia=generar_mensaje_intercepcion(tiempo_intercepcion)
    mostrar_mensaje(mensaje_policia)


def calcular_tiempo_intercepcion(velocidad_infractor, velocidad_policia,tiempo_infraccion):
    diferencia_velocidades= velocidad_policia-velocidad_infractor
    if diferencia_velocidades!=0.0:
        tiempo_intercepcion= (velocidad_infractor*tiempo_infraccion)/diferencia_velocidades

    else:
        tiempo_intercepcion=TIEMPO_INDETERMINADO

    return tiempo_intercepcion

def generar_mensaje_intercepcion(tiempo_intercepcion):
    if tiempo_intercepcion< LIMITE1:
        mensaje="NO HAY FORMA DE ALCANZAR AL INFRACTOR"

    else: 
        mensaje= f"El tiempo necesario de intercepcion es de {tiempo_intercepcion:.1}hora(S), por tanto debes "
        if tiempo_intercepcion<=LIMITE2: 
            mensaje += "SALIR EN PERSECUCION"
        elif tiempo_intercepcion<=LIMITE3: 
            mensaje +="LLAMAR AL SIGUIENTE PUESTO DE CONTROL Y SALIR EN PERSECICION"
        elif tiempo_intercepcion<=LIMITE4:
            mensaje +="UNICAMENTE LLAMAR AL SIGUIENTE PUESTO DE CONTROL"

        else: 
            mensaje+="IGNORAR EL CASO"

    return mensaje

main()


