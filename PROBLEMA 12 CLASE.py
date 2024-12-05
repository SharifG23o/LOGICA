

"""
Programa para indicar puntaje entre 0-100 y si acepta o no
Autor: Logica 01D
Fecha: Mar-2024
Liciencia: GNU GPLV3
"""

from apoyo import mostrar_mensaje,ingresar_entero, ingresar_entero_rango

PUNTAJE_MINIMO=0
PUNTAJE_MAXIMO=100
PUNTAJE_APROBADO=75

def main():
	puntuacion=ingresar_entero_rango("Ingrese puntuación: ",PUNTAJE_MAXIMO,PUNTAJE_MINIMO)
	aceptacion=determinar(puntuacion,PUNTAJE_APROBADO)
	mensaje=generar_mensaje(aceptacion)
	mostrar_mensaje(mensaje)
	
	
def ingresar_entero_rango(mensaje,maximo,minimo):
	repetir=True
	while repetir:
		valor=ingresar_entero(mensaje)
		if valor<minimo or valor>maximo:
			print(f"El valor debe estar entre {minimo} y {maximo}.")
		else:
			repetir=False
	return valor



def determinar(puntuacion,aprobacion):
	if puntuacion>aprobacion:
			aceptacion="ACEPTADO"
	else:
			aceptacion="RECHAZADO"
	return aceptacion
	

def generar_mensaje(aceptacion):
	mensaje=f"Usted fue {aceptacion}."
	return mensaje

		
main()